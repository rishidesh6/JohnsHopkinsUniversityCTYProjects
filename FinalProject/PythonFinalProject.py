#opening the file that contains all of the contacts
contactDB = open("ContactDatabase.txt", "r")
#creating a dictionary to hold the contacts, and write them back to the file when they are updated
contactDict = {}
listOfContacts = contactDB.readlines()
contactDB.close()


for line in listOfContacts:
    splitContact = line.split(":")
    contactDict[splitContact[0]] = splitContact[1].replace("\n","")

#creating the function to add or update a contact
def addOrUpdate():
    #giving the user the option to add or update a contact
    add_or_update = input('''\nDo You Want To Add Or Update A Contact?
Enter a To Add A Contact
Enter u To Update A Contact: ''')
    if add_or_update.lower() == "a":
        #if the user chose to add a contact, asking the user the name of the contact they want to add, and then checking if it exists or not before actually adding it
        name = input("\nEnter The Name Of The Contact You Want To Add Here: ")

        if doesContactExist(name) == True:
            print("This Name Already Exists On Your Contacts List, Please Enter A Different Name")
        else:
            contact = input("Enter The Email/Phone# Of The Contact You Want To Add Here: ")
            contactDict[name] = contact
            print("Sucessfully Added Contact")

    elif add_or_update.lower() == "u":
        #if the user chose to update a contact, asking the user which contact they want to update, and checking if that contact exists. If it exists, letting the user choose whether to update the name or contact, and then based on that letting them update whichever choice they picked.
        
        contactToUpdate = input("\nEnter The Name Of The Contact You Would Like To Update Here: ")

        if doesContactExist(contactToUpdate) == True:
            nameOrContact = input("Would You Like The Name Or Contact Information Of " + contactToUpdate + " To Be Updated? Enter n For The Name Or c For The Contact Information Here: ")

            if nameOrContact.lower() == "n":
                updatedName = input("\nWhat Would You Like the Name Of " + contactToUpdate + " To Be Updated To? Enter Here: ")
                updatedNamesContact = contactDict[contactToUpdate]
                del(contactDict[contactToUpdate])
                contactDict[updatedName] = updatedNamesContact
                print("Sucessfully Updated Contact")

            elif nameOrContact.lower() == "c":
                updatedContact = input("\nWhat Would You Like The Email/Phone# Of " + contactToUpdate + " To Be Updated To? Enter Here: ")
                contactDict[contactToUpdate] = updatedContact
                print("Sucessfully Updated Contact")
        else:
            print("This Contact Does Not Exist, and Therefore Cannot Be Updated")
#creating a function do display all contacts
def displayAllContacts():
    #using .read() to read out all of the current contacts in the users contact list
    print("Your Contacts")
    print("=============")
    contactDB = open("ContactDatabase.txt", "r")
    contents = contactDB.read()
    contactDB.close()
    print(contents)

#creating a function that just returns true or false if a contact exists, so that it can be used to simplify the code in the add/update and remove functions
def doesContactExist(contact):
    if contact in contactDict:
        return True
    else:
        return False

#creating a function which the user can use to search for a contact
def searchContacts(nameSearched):
    #using the doesContactExist function to see if the name searched existed or not, and then printing out the user name and contact if the name exists, or an error message if it doesnt
    if doesContactExist(nameSearched) == True:
        print("\nName: " + nameToSearch + " |" + " Contact: " + contactDict[nameToSearch])
    else:
        print("This Contact Does Not Exist")
        
#creating the delete function
def deleteContacts(contact):
    #using an if statement to see if the contact was in the dictionary which held all of the contacts, and if it was, deleting the contact, and otherwie printing an error message
    if contact in contactDict:
        del(contactDict[contact])
        print("This Contact Was Sucessfully Deleted")
    else:
        print("This Contact Is Not In Your List Of Contacts")

#creating a while True loop that runs until the user chooses to quit
while(True):
    
    print("1 - Add/Update Contact")
    print("2 - Display All Of Your Contacts")
    print("3 - Search Your Contacts")
    print("4 - Remove A Contact")
    print("5 - Quit")

    whatToDo = input("\nPlease Enter One Of The Above Options Here: ")

    #for whichever option the user selected, the program runs different functions
    if whatToDo == "1":
        addOrUpdate()
        contactDB = open("ContactDatabase.txt", "w")
        #writing out all of the contacts from the dictionary to the file using a for loop because an edit was made
        for k, v in contactDict.items():
            contactDB.write(k + ":" + v + "\n")
        contactDB.close()
        
    elif whatToDo == "2":
        displayAllContacts()
        
    elif whatToDo == "3":
        #asking the user for the name they want to search and then putting that in a variable to be used as the parameter for the search function
        nameToSearch = input("Enter The Name Of The Contact You Want To Search Here: ")
        searched = searchContacts(nameToSearch)
        
    elif whatToDo == "4":
        #asking the user which contact to delete and then putting that into a variable to be used as the parameter for the delete function
        contactToDelete = input("\nEnter The Name Of The Contact You Want To Delete Here: ")
        deleteContacts(contactToDelete)
        contactDB = open("ContactDatabase.txt", "w")
        #writing out all of the contacts from the dictionary to the file using a for loop because an edit was made
        for k, v in contactDict.items():
            contactDB.write(k + ":" + v + "\n")
        contactDB.close()
        
    elif whatToDo == "5":
        #ending the program when the user chooses to quit
        print("Thanks, bye!")
        break
    
    else:
        #making sure the user chooses a valid option
        print("\nPlease Enter One Of The Options Above")
        
