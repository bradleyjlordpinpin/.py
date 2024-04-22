choice = 'Y'
while choice == "Y":
	life = 3
	print("Your life is", life)
	print()
	print("\t 1 - Addition \n\t 2 - Subtraction \n\t 3 - Multiplication \n\t 4 - Division \n")
	op = int(input("Please select an arithmetic operation: "))
	if op == 1:
		add = num1 + num2
		num1 = print("Enter first number: ")
		num2 = print("Enter second number: ")
		a1 = int(input("Enter your Answer: "))
		if a1 == add:
			print("You won!")
		

	
	
	choice = str(input("Do you still want to continue? Y/N: "))
	print()
	