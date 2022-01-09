import zipfile
import json
import os
import datetime
import random
copyright = """###############################################################################
# BetterSpikePrime Installer
#
# INSTRUCTIONS ################################################################
#
# 1. Run this project as any project to install the hub2hub library
# 2. This project can be deleted from het hub after running it
# 3. For documenation on how to use this module see:
#    https://hub2hub.readthedocs.io/
#
###############################################################################
#
# Authors: Nard Strijbosch
# Publish date: April 11th 2021
#
# Copyright (C) 2021 Nard Strijbosch
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
###############################################################################


"""

header = """import os
import hub

install_version = '0.1.1'

files = os.listdir()
filename = 'BetterSpikePrime.py'

if filename in files:
    print('Delete old version of hub2hub library')
    os.unlink(filename)

print('Start installation')
f = open(filename, 'w')

"""

footer = """
f.close()
print("Installation was successfully finished")
print("rebooting hub")
hub.reset()
"""

filename = 'BetterSpikePrime' #specify filename
lmsFile = zipfile.ZipFile('../'+filename+"Installer.llsp", 'w') #open .lms zip archive
sourceFile = open('../'+filename+'.py') #open source from lmsExtractor

content = [] #declare array for content part of projectbody.json

for line in sourceFile.read().split('\n'):
    content.append('f.write("'+line+'\\n")\n') #write f.write for every line in content

content = "".join(content)

projectBodyJson = json.dumps({'main': copyright+header+content+footer}) #create json
tempFile = open("temp.file", 'w') #create temporary file
tempFile.write(projectBodyJson) #write json data
tempFile.close() #close temporary file
projectBodyFilesize = os.path.getsize("temp.file")
lmsFile.write("temp.file", "projectbody.json") #copy temp file to archive
os.remove("temp.file") #remove temporary file

currentDate = str(datetime.datetime.utcnow().isoformat("T"))[:-3]+"Z" #RFC-3339 format (2021-06-26T16:28:23.382Z)
print(currentDate)
manifestJson = json.dumps({ #create json for .lms manifest
    "type":"python",
    "autoDelete":False,
    "created":currentDate, #current date and time
    "id":''.join(random.choice([char for char in "abcdefghijklmnopqrstuvwyxzABCDEFGIJKLMNOPQRSTUVWXYZ1234567890_"]) for i in range(12)), #random 12 character string
    "lastsaved":currentDate,
    "size":projectBodyFilesize+551+818, #projectbody filesize + approximate manifest.json filesize + approximate icon.svg filesize
    "name":filename+"Installer",
    "slotIndex":0,
    "workspaceX":120, #default workspace values
    "workspaceY":120,
    "zoomLevel":0.5,
    "hardware":{
        "python":{
            "name":"LEGO Hub", #fake lego hub info
            "connection":"usb",
            "lastConnectedHubId":"COM4",
            "id":"COM4",
            "type":"flipper",
            "connectionState":2
        }
    },
    "state":{
        "canvasDrawerOpen":False,
        "canvasDrawerTab":"knowledgeBaseTab"
    },
    "extraFiles":[
        
    ],
    "lastConnectedHubType":"flipper"
})
tempFile = open("temp.file", 'w') #create temporary file
tempFile.write(manifestJson) #write json data
tempFile.close() #close temporary file
lmsFile.write("temp.file", "manifest.json") #copy temp file to archive
os.remove("temp.file") #remove temporary file

lmsFile.write("icon.svg", "icon.svg") #copy icon.svg to archive

lmsFile.close()
sourceFile.close()
