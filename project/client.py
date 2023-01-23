from multiprocessing.connection import Client
import os, fnmatch

def find(pattern, path):
    names = []
    paths = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                names.append(name)
                paths.append(root)
    return names,paths


address = ('localhost', 6000)
conn = Client(address)
names,paths = find('*.iso', os.getcwd())
files = [names , paths]
conn.send(files)
conn.close()
