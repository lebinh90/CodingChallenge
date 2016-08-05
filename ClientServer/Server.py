import socket
from threading import *
import pickle

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 80
print (host)
print (port)
serversocket.bind((host, port))

class client(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.start()

    def run(self):
        while 1:
            a = pickle.loads(self.sock.recv(1024).decode())
            print('Client sent:', a)
            a *= 10
            b = pickle.dumps(a)
            self.sock.send(b)
            print('Sent back:',a)

serversocket.listen(5)
print ('server started and listening')
while 1:
    clientsocket, address = serversocket.accept()
    client(clientsocket, address)
