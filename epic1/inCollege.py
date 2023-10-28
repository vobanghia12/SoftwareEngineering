'''
Team Wyoming
Fall '23
'''

# dictionary with key as username password as the value
ALL_STUDENT_ACCOUNTS = {}

# boolean to check if logged in
IsLoggedIn = false

# function for creating an account
def createAccount():
    
    username = input("Enter a unique username: ")
    while(checkUniqueUsername(username) == True):
        print("Username is already claimed. Please choose another one.\n")
        username = input("Enter a unique username: ")

    password = input("Enter a secure password: ")
    while(checkValidPassword(password) == False):
        print("Invalid password. Password must be 8-12 characters long, contain at least one capital letter, one digit,"
              " and one special character.\n")
        password = input("Enter a secure password: ")
        
    # key and value being set in dictionary
    ALL_STUDENT_ACCOUNTS[username] = password
    print("Account has been created!\n")
    return username


# function checks if user is in the dictionary and checks corresponding password returns true if found
def checkUser(username, password):
    if username in ALL_STUDENT_ACCOUNTS and ALL_STUDENT_ACCOUNTS[username] == password:
        return True
    else:
        return False


# function for login, returns null if exited or returns username if successfully logged in
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    while checkUser(username, password) != true:
        userChoice = input("Incorrect username/password. Press '1' to try again, or press anything else to exit: ")
        if userChoice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
        else:
            return
            
    return username


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
    return


# Find someone you know option
def find():
    print("\nunder construction\n")
    return


#Important links function
def importantLinks():
    print("1. A Copyright Notice")
    print("2. About")
    print("3. Accessibility")
    print("4. User Agreement")
    print("5. Privacy Policy")
    print("6. Cookie Policy")
    print("7. Copyright Policy")
    print("8. Brand Policy")
    print("9. Guest Controls")
    print("10. Languages")
    print("11. return to previous menu")

    userChoice = input("Select an option with '1' through '11': ")

    if userChoice == '1':
        print("\nunder construction\n")
        importantLinks()
    if userChoice == '2':
        print("\nunder construction\n")
        importantLinks()
    if userChoice == '3':
        print("\nunder construction\n")
        importantLinks()
    if userChoice == '4':
        print("\nunder construction\n")
        importantLinks()
    if userChoice == '5':
        print("\nunder construction\n")
        importantLinks()
    if userChoice == '6':
        print("\nunder construction\n")
        importantLinks()
    if userChoice == '7':
        print("\nunder construction\n")
        importantLinks()
    if userChoice == '8':
        print("\nunder construction\n")
        importantLinks()
    if userChoice == '9':
        print("\nunder construction\n")
        importantLinks()
    if userChoice == '10':
        print("\nunder construction\n")
        importantLinks()
    if userChoice == '11':
        return
    else:
        Print("Invalid. Please choose an option with '1' through '11'")
        importantLinks()



#useful links function
def usefulLinks():
    print("1. General")
    print("2. Browse InCollege")
    print("3. Business Solutions")
    print("4. Directories")
    print("5. Return to previous menu")

    #user input to choose option
    userChoice = input("Select an option with '1' through '5': ")

    #menu for useful links options
    if userChoice == '1':
        generalMenu()
        usefulLinks()
    elif userChoice == '2':
        print("\nunder construction\n")
        usefulLinks()
    elif userChoice == '3':
        print("\nunder construction\n")
        usefulLinks()
    elif userChoice == '4':
        print("\nunder construction\n")
        usefulLinks()
    elif userChoice == '5':
        return
    else:
        Print("Invalid. Please choose an option with '1' through '5'")
        usefulLinks()


# general menu
def generalMenu():
    print("1. Help Center")
    print("2. About")
    print("3. Press")
    print("4. Blog")
    print("5. Careers")
    print("6. Developers")
    print("7. Return to previous menu")
    if IsLoggedIn == False:
        print("8. Sign up")

    #user input to choose option
    if IsLoggedIn == False:
        userChoice = input("Select an option with '1' through '8': ")

    elif IsLoggedIn == True:
        userChoice = input("Select an option with '1' through '7': ")

    #menu for useful links options
    if userChoice == '1':
        generalMenu()
    elif userChoice == '2':
        print("InCollege was created by a group of college students in order to" 
              "help other college students connect and look for jobs.")
        generalMenu()
    elif userChoice == '3':
        print("\nunder construction\n")
        generalMenu()
    elif userChoice == '4':
        print("\nunder construction\n")
        generalMenu()
    elif userChoice == '5':
        print("\nunder construction\n")
        generalMenu()
    elif userChoice == '6':
        print("\nunder construction\n")
        generalMenu()
    elif userChoice == '7':
        return
    elif IsLoggedIn == False and userChoice == '8':
        print("1. Login")
        print("2. Create a new account")
        loginChoice = input("Choose an option with '1' or '2': ")
        if loginChoice == '1':
            username = login()
            if login is not None:
                loggedinScreen(username)
            initialScreen()
        # create account
        elif loginChoice == '2':
        # check if account limit reached
            if len(ALL_STUDENT_ACCOUNTS) >= 5:
                print("Sorry, all permitted accounts have been created. Please come back later.\n")
                initialScreen()
            else:
                username = createAccount()
                loggedinScreen(username)
                initialScreen()
    else:
        if IsLoggedIn == True:
            Print("Invalid. Please choose an option with '1' through '7'")
        if IsLoggedIn == False:
            Print("Invalid. Please choose an option with '1' through '8'")
        generalMenu()


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
        return
    else:
        print("Invalid. Please choose a valid option with '1' through '6'.\n")
        learningNewSkill()


# function for when the user is logged in
def loggedinScreen(username):
    # set isLoggedIn Boolean to true
    isLoggedIn = True
    
    # other submenu would go here
    print(" ")
    print("1. Search for a job")
    print("2. Find someone you know")
    print("3. Learn a new skill")
    print("4. View Useful Links")
    print("5. View InCollege Important Links")
    print("6. log out")

    # User choose an option
    userChoice = input("Select an option with '1', through '6': ")

    # Option menu:
    if userChoice == '1':
        jobSearch()
        loggedinScreen(username)
    elif userChoice == '2':
        find()
        loggedinScreen(username)
    elif userChoice == '3':
        learningNewSkill()
        loggedinScreen(username)
    elif userChoice == '4':
        usefulLinks()
        loggedinScreen(username)
    elif userChoice == '5':
        importantLinks()
        loggedinScreen(username)
    elif userChoice == '6':
        print("\nYou have successfully logged out\n")
        isLoggedIn = False
        return
    else:
        print("Invalid. Please choose a valid option with '1', through '6'.\n")
        loggedinScreen(username)


# function for the first screen the user sees
def initialScreen():
    print("\nWelcome to InCollege!\n")
    print("1. Login")
    print("2. Create a new account")
    print("3. View Useful Links")
    print("4. View InCollege Important Links")
    userChoice = input("Select an option with '1' through '4': ")
    # logging in
    if userChoice == '1':
        username = login()
        if login is not None:
            loggedinScreen(username)
        initialScreen()
    # create account
    elif userChoice == '2':
        # check if account limit reached
        if len(ALL_STUDENT_ACCOUNTS) >= 5:
            print("Sorry, all permitted accounts have been created. Please come back later.\n")
            initialScreen()
        else:
            username = createAccount()
            loggedinScreen(username)
            initialScreen()
    elif userChoice == '3':
        usefulLinks()
        initialScreen()
    elif userChoice == '4':
        importantLinks()
        initialScreen()
    else:
        print("Invalid. Please choose a valid option with '1' through '4'.\n")
        initialScreen()

# call main
if __name__ == '__main__':
    initialScreen()
