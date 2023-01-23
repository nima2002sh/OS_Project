from multiprocessing.connection import Listener
from multiprocessing import Process
import threading

address = ('localhost', 6000)
listener = Listener(address)
while True:
    conn = listener.accept()
    
listener.close()