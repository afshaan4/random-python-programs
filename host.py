# server.py 
import socket
import time
from subprocess import call

# create a socket object
serversocket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM) 

# set the local machine IP
host = "192.168.0.5"

#set the port
port = 9999

# bind to the port
serversocket.bind((host, port))

# queue up to 5 requests
serversocket.listen(5)

while True:
    # establish a connection
    clientsocket,addr = serversocket.accept()

    print("Got a connection from %s" % str(addr))
    currentTime = time.ctime(time.time()) + "\r\n"
    clientsocket.send(currentTime.encode('ascii'))
    cat = clientsocket.recv(1024)
    print(cat)
    cat.decode('ascii')
    if cat != None:
    	if str(cat) == 'snap':
    		print("working...")
    		call(["python3", "webcam.py"])
    clientsocket.close()