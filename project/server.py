from multiprocessing.connection import Listener
from multiprocessing import Process
import threading

address = ('localhost', 6000)
listener = Listener(address)
while True:
    conn = listener.accept()
    files = conn.recv()
    names = files[0]
    paths = files[1]
    for i in range(len(names)):
        print(names[i]," : ",paths[i])
listener.close()