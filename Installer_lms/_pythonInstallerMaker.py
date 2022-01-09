copyright = """###############################################################################
# Installation file of hub2hub (version 0.1.1)
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
# Author: Nard Strijbosch
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

filename = 'BetterSpikePrime'
installerFile = open('../'+filename+'Installer.py', 'w')
sourceFile = open('../'+filename+'.py')
installerFile.write(copyright + header)

for line in sourceFile.read().split('\n'):
    installerFile.write('f.write("'+line+'\\n")\n')

installerFile.write(footer)

installerFile.close()
sourceFile.close()
