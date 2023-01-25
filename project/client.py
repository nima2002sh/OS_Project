from multiprocessing.connection import Client
import os, fnmatch

def find():
    paths = []
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if file.endswith(".iso"):
                paths.append(os.path.join(root, file))
    return paths


address = ('localhost', 6000)
conn = Client(address)
paths = find()
conn.send("client")
conn.send(paths)
conn.close()
