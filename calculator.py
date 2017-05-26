# tha addition function
def add(a, b):
	print(a + b)

# the subtraction function
def subtract(a, b):
	print(a - b)

# the multiplication function
def mult(a, b):
	print(a * b)

#the division function
def div(a, b):
	print(a / b)

# the main function
def menu():
	choices = ['1', '2', '3', '4', '5']#the possible inputs
	choice = '0'#initialize 'choice' as 0 to start
	#the welcome message
	print("Welcome to the calculator")
	print(" ")
	print("to do an addition type 1")
	print("to do a subtraction type 2")
	print("to do a multiplication type 3")
	print("to do a division type 4")
	print("to exit type 5")
	# the main loop
	while True:
		# the User Interface
		choice = input(">>> ")#the main prompt 

		if choice == '1':
			a = int (input("enter a number > "))
			b = int (input("enter the second number > "))
			add(a, b)


		elif choice == '2':
			a = int (input("enter a number > "))
			b = int (input("enter the second number > "))
			subtract(a, b)

		elif choice == '3':
			a = int (input("enter a number > "))
			b = int (input("enter the second number > "))
			mult(a, b)

		elif choice == '4':
			a = int (input("enter a number > "))
			b = int (input("enter the second number > "))
			div(a, b)

		elif choice == '5':
			exit()
		choice = '0' # reset choice to zero

menu()#start the program