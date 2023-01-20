from multiprocessing.connection import Listener

address = ('localhost', 6000)
listener = Listener(address)
conn = listener.accept()
listener.close()