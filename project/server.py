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
    
    coneccted = True

    while coneccted:
        try:
            path = conn.recv()
            path_list.put(path)

        except (EOFError , ConnectionResetError):
            coneccted = False
            print("conection lost")


def worker_handler(conn):

    while True:
        while path_list.qsize()>=5:
            p = []
            for i in range(t):
                p.append(path_list.get())
            conn.send(p)

        r = path_list.qsize()%t

        if r:
            p = []
            for i in range(r):
                p.append(path_list.get())
            conn.send(p)



if __name__ == "__main__":

    path_list = Queue()
    t = 5
    
    address = ('localhost', 6000)
    listener = Listener(address)

    for i in range(t):
        Thread(target=make_worker).start()

    while True:
        conn = listener.accept()
        massage = conn.recv()
        if massage == "worker":
            Thread(target=worker_handler, args=[conn]).start()
        elif massage == "client":
            Thread(target=commander_handler, args=[conn]).start()

    conn.close()
