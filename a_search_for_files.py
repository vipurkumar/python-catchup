"""
 Search for files with a given name on the file system
"""
import os

filename = input('Name of the file extension to search for: ')
path = input('Drive/directory where to start searching: ')
if path == '':
    path = '.'   # current directory

for dirname, subdirs, files in os.walk(path):
    dirname = dirname.replace('\\', '/')
    for f in files:
        if f.endswith(filename):
            print('\tFound file', dirname+'/'+f)
    for d in subdirs:
        if d.endswith(filename):
            print('\tFound directory', dirname+'/'+d)
