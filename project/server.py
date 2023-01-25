from multiprocessing.connection import Listener
from threading import Thread
from multiprocessing import Process
from queue import Queue
import threading
import hashlib
import worker



def make_worker():
    while True:
        worker_proc = Process(target=worker.worker)
        worker_proc.start()
        worker_proc.join()

def commander_handler(conn):
    while True:
        paths = conn.recv()
        path_list.put(paths)

def worker_handler(conn):
    while True:
        paths = path_list.get()
        conn.send(paths)


if __name__ == "__main__":

    path_list = Queue()
    
    address = ('localhost', 6000)
    listener = Listener(address)

    for i in range(5):
        Thread(target=make_worker).start()

    while True:
        conn = listener.accept()
        massage = conn.recv()
        if massage == "worker":
            Thread(target=worker_handler, args=[conn]).start()
        elif massage == "client":
            Thread(target=commander_handler, args=[conn]).start()
    conn.recv()
    conn.send(paths)
    conn.close()
