def save(li): # the save function
	with open('list.txt', 'w') as f:
		f.write(li)
	print("saved!!!")#print "saved!!!" when its done saving

def read():#the function to open your list and prints it to the screen
	with open('list.txt', "r") as f:
		contents = f.read()
	return contents


def menu():#the UI
	choice = '0'#initialize 'choice' as 0 to start
	
	#the welcome message
	print("Welcome to Listmaker")
	print(" ")
	print("To add stuff to your list type 1")
	print("To read your list type 2")
	print("To exit type 5")

	# the main loop
	while True:
		choice = input(">>> ")#the main prompt 

		if choice == '1':#if choice is 1 
			print("type in list entries seperated by commas")
			print("when done hit enter") 
			stuff = input("# ")#takes their input
			out = str(stuff.split(','))#turns it into a list then a string (easier than formatting)
			save(out)#

		elif choice == '2':#if choice is 2 
			print("your list:")
			contents = read()#open the file
			print(contents)#print it to the screen

		elif choice == '5':#if choice is 5
			exit()#exit

		choice = '0' # reset choice to zero at the end of each loop

menu()#call the menu