#!/usr/bin/python3
#import need library
import re
import csv

#the function which will be called when geting the file
def getFile():
	sortContact = []
        #load it if the file exists
	try:
		with open('addressbook.csv', 'r') as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			for row in csv_reader:
                		sortContact.append(row)
        #ask to create the file
	except:
		userinput = input("\nWe need to create a file to store the address book, Do you want to create one now? [y/n]\n")
		if confirming(userinput):
			with open('addressbook.csv', 'w')as csv_file:
				writer = csv.writer(csv_file)
				menu()
		else:
			print("\nSorry, we cannot do anything without a storing file")
			exit()
	return sortContact

#rewrite the file, called when sorts, deletes or edits contacts.
def writeFile(data):
	with open('addressbook.csv', 'w')as csv_file:
		writer = csv.writer(csv_file)
		for row in data:
			writer.writerow(row)

#appending the file, called when adding a new contact
def appandFile(data):
	with open('addressbook.csv', 'a')as csv_file:
		writer = csv.writer(csv_file)
		for row in data:
			writer.writerow(row)
#registration for columns which require a number input
def checkNum(inputVal):
	while not re.match("^[0-9 \-]+$", inputVal):
		inputVal = input("Error! Make sure you only use numbers or '-' .\n")
	return inputVal

#registration for columns which require a string input
def checkLetter(inputVal):
	while not re.match("^[a-zA-Z]+$", inputVal):
		inputVal = input("Error! Please type in a valid name.\n")
	return inputVal
#registration for the email column which requires a email format input
def checkEmail(inputVal):
	while not re.match("[^@]+@[^@]+\.[^@]+$", inputVal):
		inputVal = input("Error! Please type in a valid email addresss.\n")
	return inputVal

##registration for the Date of Birth column which requires a dd-mm-yyyy format input
def checkDOB(inputVal):
	while not re.match("^([0-2][0-9]|(3)[0-1])(\-)(((0)[0-9])|((1)[0-2]))(\-)\d{4}$", inputVal):
		inputVal = input("Error! Please type in a valid data of birth with the format of 'dd-mm-yyyy'.\n")
	return inputVal

#this function is only used for the ID column which checks if the ID is exist already
def CheckIdUnique(inputVal):
	checking = False
	data = getFile()
	while checking == False:
		inputVal = checkNum(inputVal)
		if len(data) == 0:
			break 
		for checkUnique in data:
			if inputVal == checkUnique[0]:
				checking = False
				break
			else:
				checking = True
		if checking == False:
			inputVal = input("Warning! This ID has been taken, please enter another one.\n")
		else:
			break
	return inputVal

# Adding function which gets the user input then confirm, then add it to the csv file using appendFile method
def adding():
	record = []
	ID = input("ID: ")
	ID = CheckIdUnique(ID)#must be a unique and a number input
	firstname = input("First name: ")
	firstname = checkLetter(firstname)#must be a string input
	lastname = input("Last name: ")
	lastname = checkLetter(lastname)#must be a string input
	address = input("Address: ")
	DOB = input("Date of Birth: ")
	DOB = checkDOB(DOB)#must be the dd-mm-yyyy format and a number input
	amount = input("Donated Amount: ")
	amount = checkNum(amount)#must be aa number input
	phone = input("Phone number: ")
	phone = checkNum(phone)#must be aa number input
	email = input("Email Address: ")
	email = checkEmail(email)
	contact = [ID, firstname, lastname, address, DOB, amount, phone, email]
	print()
	print(contact)
	userinput = input("\nPlease comfirm, correct or not? [y/n]\n")
	if confirming(userinput):
		record.append(contact)
		appandFile(record)
		print("\nThe contact has been added.")
	restart()
	
#This function will be called each time when trying to show the address book contacts
def showing():
	readFile = getFile()
	print("\nID/First Name/Last Name/Address/Date of Birth/Donated Amount/Phone Number/Email")	
	print("--------------------------------------------------------------------------------")
	for line in readFile:
		print(','.join(line))

#delete option whcih read user input of ID first them confirm if the user want to delete it, if yes, delete it.
def deleting():
	showing()
	colDelete = input("Please enter the ID of the contact to delete.\n")
	data = getFile()
	ids = []
		
	
	lineToDelete = ''

	for line in data:
		if colDelete == line[0]:
			ids.append(line[0])
			print(','.join(line))
			userinput = input("\nAre you sure you want to delete this contact? [y/n]\n")
			if confirming(userinput):
				lineToDelete = line
			else:
				restart()
	if len(ids) == 0:
		print("\nCould not find a contact with the ID "+ colDelete +"!")
		restart()
	data.remove(lineToDelete)
	writeFile(data)
	if lineToDelete == '':
		print("\nCannot find the contact with ID "+ colDelete +" !")
		restart()
	print("\nThe contact has been deleted from the address book.")
	restart()

#searching option which searches the file line by line, and comes up with all occurances
def searching():
	showing()
	readFile = getFile()
	searchContact = []
	criteria = input("Please enter a keyword to search.\n")
	print()
	for line in readFile:
		line = ','.join(line)
		if criteria in line:
			searchContact.append(line)
			print(line)
	if len(searchContact) == 0:
		userinput = input("Sorry, did not find any matched information, do you want to search again?  [y/n]\n")
		if confirming(userinput):
			searching()
	else:
		print("\nFound "+ str(len(searchContact)) +" item(s) above with your keyword")
	restart()

#editing option which reads the user input of ID first to find the right contact to edit, then the user will be asked that which column is he trying to edit and what it will be, then confirm it, if yes, change it.
def editing():
	showing()
	data = getFile()
	editCol = input("Please enter the ID of the contact to edit.\n")
	colToEdit = ''
	editTo = ''
	oldValue = ''
	getCol=''
	ids = []
	for line in data:
		if editCol == line[0]:
			ids.append(line[0])
			print(','.join(line))
			colToEdit = input("\nWhich column do you want to change?\n")
			if colToEdit.lower() == 'id':
				getInput = input("Sorry, You cannot change the ID, Do you want to try again?  [y/n]\n")
				if confirming(getInput):
					editing()
				else:
					restart()
			getCol = findCol(colToEdit)
			editTo = input("\nWhat do you want it to be changed to?\n")
			if getCol[1] == 'First Name' or getCol[1] == 'Last Name':
				editTo = checkLetter(editTo)
			elif getCol[1] == 'Donated Amount' or getCol[1] == 'Phone Number':
				editTo = checkNumber(editTo)
			elif getCol[1] == 'Date Of Birth':
				editTo = checkDOB(editTo)
			elif getCol[1] == 'Email':
				editTo = checkEmail(editTo)

			oldValue = line[getCol[0]]
			line[getCol[0]] = editTo
	if len(ids) == 0:
		print("\nCould not find a contact with the ID "+ editCol +"!")
		restart()

	userinput = input("\nAre you sure you want to change the column " + getCol[1] + " from " + oldValue + " to " + editTo + " for the ID " + editCol + "? [y/n]\n" )
	if confirming(userinput):
		writeFile(data)
		print( "\n" + getCol[1] + " of the ID " + editCol + " has been successfuly changed to " + editTo)
	restart()

#confirming function will be called everytime when asking user input of yes or no
def confirming(YorN):
	YorN = YorN.lower()
	if YorN == 'y':
		return True
	elif YorN == 'n':
		return False
	else:
		print("Invalid command!")
		restart()
#this function will called to find the right column and ignores the input letter case, which is called in 
def findCol(col):
	col = col.lower()
	if col == 'id':
		return [0,'ID']
	elif col == 'first name':
		return [1,'First Name']
	elif col == 'last name':
		return [2,'Last Name']
	elif col == 'address':
		return [3,'Address']
	elif col == 'date of birth':
		return [4,'Date Of Birth']
	elif col == 'donated amount':
		return [5,'Donated Amount']
	elif col == 'phone number':
		return [6,'Phone Number']
	elif col == 'email':
		return [7,'Email']
	else:
		print("\nCould not find the column. Please use value in ID/First Name/Last Name/Address/Date of Birth/Donated Amount/Phone Number/Email")
		restart()

#sorting option which asks the user input of whcih column if the user tring to sort with, then sort through
def sorting():
	showing()
	colSort = input("Which column above do you want to sort with?\n")
	getCol = findCol(colSort)
	data = getFile()
	data = sorted(data, key=lambda x: x[getCol[0]])
	writeFile(data)
	print("\nThe address book has been sorted with " + getCol[1])
	restart()

#find best option which finds the highest number in the donation cloumn then print it out
def findBest():
	best = 0
	name = ''
	data = getFile()
	for bestDonate in data:
		if float(bestDonate[5]) > best:
			best = float(bestDonate[5])
			name = bestDonate[1] + ' ' + bestDonate[2]
	print("The best donate is $" + ("%.2f" % best) + ' from ' + name)
	restart()

# The main menu
def menu():
	print("-------------------------------------------------------------")
	print("|                                                           |")
	print("|                  Charity Address Book                     |")
	print("|                                                           |")
	print("----------------------------Menu-----------------------------")
	print("|                                                           |")
	print("|                   1.   Add Contact                        |")
	print("|                   2.   Delete Contact                     |")
	print("|                   3.   Search Contact                     |")
	print("|                   4.   Edit Contact                       |")
	print("|                   5.   Sort Contact                       |")
	print("|                   6.   Best Donate                        |")
	print("|                   7.   Quit                               |")
	print("|                                                           |")
	print("-------------------------------------------------------------")
	choice = input("Choose a option above!\n")
	if choice == '1':
		print("\nYou have chosen to add a contact.\n")
		adding()
	elif choice == '2':
		print("\nYou have chosen to delete a contact.\n")
		deleting()
	elif choice == '3':
		print("\nYou have chosen to search a contact.\n")
		searching()
	elif choice == '4':
		print("\nYou have chosen to edit a contact.\n")
		editing()
	elif choice == '5':
		print("\nYou have chosen to sort the address book.\n")
		sorting()
	elif choice == '6':
		print("\nYou have chosen to find the best donate.\n")
		findBest()
	elif choice == '7':
		print("\nYou have chosen to quit the program.\n")
		print("-------------------------------------------------------------------")
		print("|            Thank you for using the charity address book         |")
		print("-------------------------------------------------------------------")
		exit()
	else:
		print("\nInvalid command\n")
		restart()
def restart():
	userinput = input("\nWould you like to restart the program to perform another operation? [y/n]\n")
	if confirming(userinput):
		menu()
	else:
		print("-------------------------------------------------------------------")
		print("|            Thank you for using the charity address book         |")
		print("-------------------------------------------------------------------")
		exit()

# The start of the program, load the file first, then go to the main menu
getFile()
menu()
