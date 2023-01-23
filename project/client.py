from multiprocessing.connection import Client
import os, fnmatch

def find(pattern, path):
    matchfiles = {}
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                matchfiles[name] = root
    return matchfiles


address = ('localhost', 6000)
conn = Client(address)
files = find('*.iso', os.getcwd())
print(files)
conn.send(files)
conn.close()
