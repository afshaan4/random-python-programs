from datetime import datetime #import the date and time module
from time import sleep #import the sleep module
import random #import the random module

log = open("log.txt", "w") #open a file

for i in range(5): #for loop 
	now = str(datetime.now())
    # make some random data from 0 to  1024
	data = random.randint(0, 1024)
	log.write(now + " " + str(data) + "\n")# write the time and data to the file
	print(".")#print a full stop
	sleep(.9)#sleep
log.flush()#clear log
log.close()#close it