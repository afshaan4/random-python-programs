import sys

if (len(sys.argv) != 2):
	print("Usage: python3 fileReader.py filename")
	sys.exit()

scriptname = sys.argv[0]
filename = sys.argv[1]

file = open(filename, "r")
lines = file.readlines()
file.close()

for line in lines:
	print(line, end = '')
