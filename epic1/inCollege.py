'''
Team Wyoming
Fall '23
'''

# dictionary with key as username password as the value
ALL_STUDENT_ACCOUNTS = {}
ALL_JOBS = {}


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

    firstName = input("First Name: ")
    lastName = input("Last Name: ")

    # key and value being set in dictionary
    """Change the way system stores account information to a dictionary with the username as the key and information of username (password, firstName, lastName) as value"""
    ALL_STUDENT_ACCOUNTS[username] = {
        'password': password,
        'firstName': firstName,
        'lastName': lastName,
    }

    print("Account has been created!\n")


# function checks if user is in the dictionary and checks corresponding password returns true if found
def checkUser(username, password):
    if username in ALL_STUDENT_ACCOUNTS and ALL_STUDENT_ACCOUNTS[username]['password'] == password:
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


def postJob():
    title = input("Job's title: ")
    description = input("Job's description: ")
    employer = input("Employer's name: ")
    location = input("Job's location: ")
    salary = input("Job's salary: ")

    if len(ALL_JOBS) >= 5:
        print("Sorry, all permitted jobs have been created. Please come back later.\n")
        jobSearch()
    else:
        ALL_JOBS[title] = {
            'description': description,
            'employer': employer,
            'location': location,
            'salary': salary,
        }

        jobSearch()

# Job search/Internship Option
def jobSearch():
    print("1. Search for a job/internship")
    print("2. Post a job/internship")
    print("3. Return to main menu")

    # User choose an option
    userChoice = input("Select an option with '1', '2', or '3': ")

    # Option menu:
    if userChoice == '1':
        print("\nunder construction\n")
        jobSearch()
    elif userChoice == '2':
        postJob()
        jobSearch()
    elif userChoice == '3':
        loggedinScreen()
    else:
        print("Invalid. Please choose a valid option of either '1', '2', or '3'.\n")
        jobSearch()


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

def findPeople():
    firstName = input("First Name: ")
    lastName = input("Last Name: ")

    for i in ALL_STUDENT_ACCOUNTS:
        if firstName == i.firstName and lastName == i.lastName:
            print("They are a part of the InCollege system.\n")
    
    print("They are not yet a part of the InCollege system yet.\n")

    preLoggedInScreen()

def logIn():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if checkUser(username, password):
        print("You have successfully logged in.\n")
        loggedinScreen()
    else:
        print("Incorrect username/password. Please try again.\n")
        initialScreen()

#function for the marketing before the user login
def preLoggedInScreen():
    print("Success story: Congratulations!!! A USF student has successfully landed an internship for the Summer 2024 with the help of InCollege!\n")
    print("Select one of the following options:")
    print("1. Find out why you would want to join InCollege")
    print("2. Find out who has joined InCollege")
    print("3. Login into your account")
    print("4. Return to the previous screen")

    userChoice = input("Select an option with '1', '2', '3', or '4': ")

    if userChoice == "1":
        print("Video is now playing")
    elif userChoice == "2":
        findPeople()
    elif userChoice == "3":
        logIn()
    elif userChoice == "4":
        initialScreen()
    else:
        print("Invalid. Please select one of the following options: '1', '2', '3', or '4'.\n")
        preLoggedInScreen()
    
# function for the first screen the user sees
def initialScreen():
    print("\nWelcome to InCollege!\n")
    print("1.Login")
    print("2.Create a new account")
    userChoice = input("Select an option with '1' or '2': ")
    # logging in
    if userChoice == '1':
        preLoggedInScreen()
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