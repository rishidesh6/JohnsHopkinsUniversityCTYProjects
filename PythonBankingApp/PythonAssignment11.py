#everything without comments was from my previous assingment's code
#I used the previous assignment's code to get the features that I had already made,such as the deposit and withdrawal functions, and the login screen. I added the two functions to store the user accounts in a seperate txt file.
accDictionary = {}



def ID_Available_Or_Not(UserID):
    for key, value in accDictionary.items():
        if key == UserID:
            return True   
    return False


def deposit(dep, userID):
    account = accDictionary[userID]
    account = dep + account
    return account
    
def withdrawal(withdraw, userID):
    account = accDictionary[userID]
    account = account - withdraw
    if account < 0.0:
        print("You don't have enough funds in your account")
        print("\n")
        account = account + withdraw
        return account
    else:
        return account

def customerBalance(key, value):
    print("Customer Name: " + str(key))
    print("Customer Balance: " + str(value))
    
  

def loopUntilQuit():
    quitOrNot = str(input('''Type 1 If You Want To Make A Deposit,
Type 2 If You Want To Make A Withdrawal,
Type 9 If You Want To Quit: \n'''))
    return quitOrNot

#creaing a new function to read the lines from the file to turn into accounts
def readFromFile():
    database = open('./PyBankDatabase.txt', 'r')
    #using a for loop to split each line in the file, and then turning them into entries in the dictionary, and replacing the \n from the file with a blank space
    for line in database.readlines():
        splitLines = line.split(",")
        accDictionary[splitLines[0]] = float(splitLines[1].replace("\n",""))

#creating a new function to write to the file
#this function rewrites every entry of the dictionary into the file, as entries change with deposits, withdrawals, and new accounts
def writeToFile():
    database = open('./PyBankDatabase.txt', 'w')
    #uses a for loop to write back to the database in the right format(name, balance)
    for key, value  in accDictionary.items():
        database.write(key + "," + str(value) + "\n")
        

#calling this function to create the entries in the dictionary from the database file
readFromFile()

user = ""
loggedIn = False
while True:
    #I added a third option to the login screen for the user to completely quit the program
    print("Welcome To PyBank!")
    print("------------------")
    print("------------------\n")
    logIn_or_createAccount = input('''Press 1 If You Want To Log In...
Press 2 If You Want To Create A New Account...
Press 3 If You Want To Quit The Program''')

    if logIn_or_createAccount == "1":
        user = input("Please Type Your Name Here: ")
        if ID_Available_Or_Not(user):
            customerBalance(user, accDictionary[user])
            loggedIn = True
        else:
            print("\n This Account Name Does Not Exist, Please Retype Your Name /n")
            
    elif logIn_or_createAccount == "2":
        user = input("Hello, Please Enter Your Name For This Account: ")
        if ID_Available_Or_Not(user):
            print("\n This Name Is Already Being Used In An Existing Account, Please Type A Different Name \n")
            
        else:
            accDictionary[user] = 0.0
            print("\n")
            customerBalance(user, accDictionary[user])
            loggedIn = True
    elif logIn_or_createAccount == "3":
        break
    else:
        print("\n Please Press Either 1 Or 2! \n")
    if bool(loggedIn):
        loop = loopUntilQuit()

        if loop == "1":
            depositAmount = float(input("Please Enter The Amount You Want To Deposit Here: "))
            newAccBalance = deposit(depositAmount, user)
            accDictionary[user] = newAccBalance
            print("\n")
            customerBalance(user, accDictionary[user])
        
        elif loop == "2":
            withdrawalAmount = float(input("Please Enter The Amount You Want To Withdraw Here: "))
            newBalance = withdrawal(withdrawalAmount, user)
            accDictionary[user] = newBalance
            print("\n")
            customerBalance(user, accDictionary[user])

        elif loop == "9":
            print("Thank You For Working With Us!!!\n")

    loggedIn= False
#calling this function after the loop has taken place, as new entries have been created, or entries may have been updated
#this will rewrite all of the updated and new entries into the database file
writeToFile()
