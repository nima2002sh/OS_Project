from multiprocessing.connection import Client

address = ('localhost', 6000)
conn = Client(address)

conn.close()