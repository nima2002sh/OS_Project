from multiprocessing.connection import Client
import hashlib
import random

address = ('localhost', 6000)

def calmd5(path):
    with open(path, "rb") as f:
        file_hash = hashlib.md5()

        while chunk := f.read(8192):
            file_hash.update(chunk)

    return file_hash.hexdigest()

def worker():
    with Client(address) as w:
        w.send("worker")

        while True:
            paths = w.recv()
            for path in paths:
                if random.randint(1, 3) == 3:
                    md5 = " "
                else:
                    md5 = calmd5(path)
                with open(path+".md5" , "w") as m:
                    m.write(md5)


if __name__ == "__main__":
    worker()