from multiprocessing.connection import Client
from threading import Thread , Lock
from queue import Queue
import os
import hashlib

def calmd5(path):
    with open(path, "rb") as f:
        file_hash = hashlib.md5()

        while chunk := f.read(8192):
            file_hash.update(chunk)

    return file_hash.hexdigest()

def find():
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if file.endswith(".iso"):
                path_list.put(os.path.join(root, file))


def check():
    while True:
        path = path_list.get()
        if os.path.exists(path+".md5"):
            with open(path+".md5" , "r") as m:
                if m.read() != calmd5(path):
                    print("md5 changed : " + path)
        else: 
            lock.acquire()
            conn.send(path)
            lock.release()


if __name__ == "__main__":
    address = ('localhost', 6000)
    conn = Client(address)

    path_list = Queue()
    lock = Lock()

    Thread(target=find).start()

    conn.send("client")

    for i in range(5):
        Thread(target=check).start()
