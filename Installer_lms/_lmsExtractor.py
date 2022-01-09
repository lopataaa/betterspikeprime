import zipfile
import json

pythonFile = open('../betterspikeprime_src.py', 'w')
archive = zipfile.ZipFile('../betterspikeprime_src.lms', 'r')
MSFile = archive.open('projectbody.json')
content = json.loads(MSFile.read())

for line in content['main'].split('\n'):
    if '### end of library definition ###' in line:
        break
    pythonFile.write(line+'\n')

pythonFile.close()
MSFile.close()
archive.close()
