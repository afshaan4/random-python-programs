# client.py  
import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = "192.168.0.5"

#ste the port
port = 9999

# connection to hostname on the port.
s.connect((host, port))

# Receive no more than 1024 bytes
tm = s.recv(1024)

cat = input("type a message > ")
#send something
s.send(cat.encode('ascii'))

s.close()

print("The time got from the server is %s" % tm.decode('ascii'))
