choice = 'Y'
while choice == "Y":
	age1 = int(input("Enter first age: "))
	age2 = int(input("Enter second age: "))
	age3 = int(input("Enter third age: "))
	print()
		
	if age2 < age1 > age3:
		print("Oldest is", age1)
		if age2 > age1 < age3:
			print("Youngest is ", age1)
		elif age1 > age2 < age3:
			print("Youngest is ", age2)
		else:
			age1 > age3 < age2
			print("Youngest is ", age3)
	elif age1 <  age2 > age3:
		print("Oldest is ", age2)
		if age2 > age1 < age3:
			print("Youngest is ", age1)
		elif age1 > age2 < age3:
			print("Youngest is ", age2)
		else:
			age1 > age3 < age2
			print("Youngest is ", age3)
	else:
		age1 < age3 > age2
		print("Oldest is ", age3)
		if age2 > age1 < age3:
			print("Youngest is ", age1)
		elif age1 > age2 < age3:
			print("Youngest is ", age2)
		else:
			age1 > age3 < age2
			print("Youngest is ", age3)
			
	print()
	choice = str(input("Do you still want to continue? Y/N: "))
	print("-----------------------------------------------------------------------")