from multiprocessing.connection import Client
import os, fnmatch

def find(pattern, path):
    paths = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                paths.append(os.path.abspath(name))
    return paths


address = ('localhost', 6000)
conn = Client(address)
paths = find('*.iso', os.getcwd())
conn.send("client")
conn.send(paths)
conn.close()
