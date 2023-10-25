'''
Team Wyoming
Fall '23
'''

# dictionary with key as username password as the value
ALL_STUDENT_ACCOUNTS = {}


# function for creating an account
def createAccount():
    username = input("Enter a unique username: ")
    if checkUniqueUsername(username) == True:
        print("Username is already claimed. Please choose another one.\n")
        createAccount()
        return

    password = input("Enter a secure password: ")
    if checkValidPassword(password) == False:
        print("Invalid password. Password must be 8-12 characters long, contain at least one capital letter, one digit,"
              " and one special character.\n")
        createAccount()
        return

    # key and value being set in dictionary
    ALL_STUDENT_ACCOUNTS[username] = password
    print("Account has been created!\n")


# function checks if user is in the dictionary and checks corresponding password returns true if found
def checkUser(username, password):
    if username in ALL_STUDENT_ACCOUNTS and ALL_STUDENT_ACCOUNTS[username] == password:
        return True
    else:
        return False


# function checks if username is unique in the dictionary
def checkUniqueUsername(username):
    if username in ALL_STUDENT_ACCOUNTS:
        return True
    else:
        return False


# checks if inputted password during creation is within our requirements
def checkValidPassword(password):
    # do this if it is valid length
    if 8 <= len(password) <= 12:
        checkDigit = False
        checkSpecialCharacter = False
        checkUpperCase = False

        # check if it has the password requirements
        for x in password:
            if x.isdigit():
                checkDigit = True
            elif x in "!@#$%^&*()_+[]:;<>,.?~":
                checkSpecialCharacter = True
            elif x.isupper():
                checkUpperCase = True
        # if all correct then it should return as 'true' if one of them is wrong the and statements turn false
        return checkUpperCase and checkDigit and checkSpecialCharacter
    # do this if length is invalid
    else:
        return False


# Job search/Internship Option
def jobSearch():
    print("\nunder construction\n")
    loggedinScreen()


# Find someone you know option
def find():
    print("\nunder construction\n")
    loggedinScreen()


# Learn a new skill option
def learningNewSkill():
    print("1. Python")
    print("2. Java")
    print("3. C++")
    print("4. C#")
    print("5. SQL")
    print("6. return to main menu")

    # User choose an option
    userChoice = input("Select an option with '1' through '6': ")

    # Option menu:
    if userChoice == '1':
        print("\nunder construction\n")
        learningNewSkill()
    elif userChoice == '2':
        print("\nunder construction\n")
        learningNewSkill()
    elif userChoice == '3':
        print("\nunder construction\n")
        learningNewSkill()
    elif userChoice == '4':
        print("\nunder construction\n")
        learningNewSkill()
    elif userChoice == '5':
        print("\nunder construction\n")
        learningNewSkill()
    elif userChoice == '6':
        loggedinScreen()
    else:
        print("Invalid. Please choose a valid option with '1' through '6'.\n")
        learningNewSkill()


# function for when the user is logged in
def loggedinScreen():
    # other submenu would go here
    print("")
    print("1. Search for a job")
    print("2. Find someone you know")
    print("3. Learn a new skill")
    print("4. log out")

    # User choose an option
    optionChoice = input("Select an option with '1', '2', '3', or '4': ")

    # Option menu:
    if optionChoice == '1':
        jobSearch()
    elif optionChoice == '2':
        find()
    elif optionChoice == '3':
        learningNewSkill()
    elif optionChoice == '4':
        print("\nYou have successfully logged out\n")
        initialScreen()
    else:
        print("Invalid. Please choose a valid option of either '1', '2', or '3'.\n")
        loggedinScreen()


# function for the first screen the user sees
def initialScreen():
    print("\nWelcome to InCollege!\n")
    print("1.Login")
    print("2.Create a new account")
    userChoice = input("Select an option with '1' or '2': ")
    # logging in
    if userChoice == '1':
        username = input("Enter username: ")
        password = input("Enter password: ")
        if checkUser(username, password):
            print("You have successfully logged in.\n")
            loggedinScreen()
        else:
            print("Incorrect username/password. Please try again.\n")
            initialScreen()
    # create account
    elif userChoice == '2':
        # check if account limit reached
        if len(ALL_STUDENT_ACCOUNTS) >= 5:
            print("Sorry, all permitted accounts have been created. Please come back later.\n")
            initialScreen()
        else:
            createAccount()
            loggedinScreen()
    else:
        print("Invalid. Please choose a valid option of either '1' or '2'.\n")
        initialScreen()

# call main
if __name__ == '__main__':
    initialScreen()