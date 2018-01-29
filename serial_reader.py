#code to recieve data over USB
import serial

port = input("Port the arduino is connected to > ")
baudRate = int(input("baud rate to use > "))
arduino = serial.Serial(port, baudRate, timeout=.1)
while True:
	data = arduino.readline()[:-2] #the last bit gets rid of the new-line chars
	if data:
		formattedData = str(data.split( ))
		print (formattedData)

