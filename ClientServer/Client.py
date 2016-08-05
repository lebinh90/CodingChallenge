import socket,sys,pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host ="localhost"
port = 80
s.connect((host,port))

def sendvalue(string):
   s.send(pickle.dumps(r))
   data = pickle.loads(s.recv(1024).decode())
   print (data)

while 2:
   try:
       r = int(raw_input('enter a number: '))
       sendvalue(s)
   except ValueError, e:
       print "Empty value or not an int", + str(e)
       sys.exit(1)
   finally:
       break
       s.close()
