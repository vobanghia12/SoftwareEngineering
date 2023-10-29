'''
Team Wyoming
Fall '23
'''

# dictionary with key as username password as the value
ALL_STUDENT_ACCOUNTS = {}
ALL_JOBS = {}

# global variable to track current user (also used to check if user is logged in or not)
globalUsername = None

searchList = []


# function for creating an account
def createAccount():
    # input username and check if unique
    username = input("Enter a unique username: ")
    while (checkUniqueUsername(username) == True):
        print("Username is already claimed. Please choose another one.\n")
        username = input("Enter a unique username: ")

    # input password and check if valid
    password = input("Enter a secure password: ")
    while (checkValidPassword(password) == False):
        print("Invalid password. Password must be 8-12 characters long, contain at least one capital letter, one digit,"
              " and one special character.\n")
        password = input("Enter a secure password: ")

    # input first name and force re-input while empty
    firstName = input("Enter your first name: ")
    while firstName is None:
        firstName = input("Invalid, Enter your first name: ")

    # input last name and force re-input while empty
    lastName = input("Enter your last name: ")
    while lastName is None:
        lastName = input("Invalid, Enter your last name: ")

    # input university and force re-input while empty
    university = input("Enter your university: ")
    while university is None:
        university = input("Invalid, Enter your university: ")

    # input major and force re-input while empty
    major = input("Enter your major: ")
    while major is None:
        major = input("Invalid, Enter your major: ")

    # Key is the username, values are password, firstName, lastName, university, major, Language
    # also holds booleans for SMS, Email and Advertising, as well as lists for friends and friend requests
    ALL_STUDENT_ACCOUNTS[username] = {
        'password': password,
        'firstName': firstName,
        'lastName': lastName,
        'university': university,
        'major': major,
        'Language': 'English',
        'SMS': True,
        'Email': True,
        'Advertising': True,
        'friends': [],
        'requests': []
    }

    print("Account has been created!\n")
    # return username to keep track of current user
    return username


# function checks if user is in the dictionary and checks corresponding password returns true if found
def checkUser(username, password):
    if username in ALL_STUDENT_ACCOUNTS and ALL_STUDENT_ACCOUNTS[username]['password'] == password:
        return True
    else:
        return False


# function for login, returns null if exited or returns username if successfully logged in
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    while checkUser(username, password) != True:
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


# Fuction for Posting a job
def postJob():
    title = input("Job's title: ")
    description = input("Job's description: ")
    employer = input("Employer's name: ")
    location = input("Job's location: ")
    salary = input("Job's salary: ")
    # sets 'poster' variable to the first and last name of the person who posted it with a space inbetween
    poster = ALL_STUDENT_ACCOUNTS[globalUsername]['firstName'] + ' ' + ALL_STUDENT_ACCOUNTS[globalUsername]['lastName']

    if len(ALL_JOBS) >= 5:
        print("Sorry, all permitted jobs have been created. Please come back later.\n")
        return
    else:
        # creates job with all attributes defined above
        ALL_JOBS[title] = {
            'description': description,
            'employer': employer,
            'location': location,
            'salary': salary,
            'poster': poster
        }

        return


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
        return
    else:
        print("Invalid. Please choose a valid option of either '1', '2', or '3'.\n")
        jobSearch()


# Find someone you know option
def find():
    # uses globalUsername variable to check if user is not logged in
    if globalUsername is None:
        firstName = input("First Name: ")
        lastName = input("Last Name: ")

        # search through all users to check if they are a part of the system
        for username in ALL_STUDENT_ACCOUNTS:
            if firstName == ALL_STUDENT_ACCOUNTS[username]['firstName'] and lastName == ALL_STUDENT_ACCOUNTS[username][
                'lastName']:
                print("They are a part of the InCollege system.\n")
                return

        print("They are not a part of the InCollege system yet.\n")
        return
    # if user is logged in, allows for sending friend requests
    elif globalUsername is not None:

        # list to add found users
        searchList = []

        print("1. Search for a user by Last Name")
        print("2. Search for a user by University")
        print("3. Search for a user by Major")
        print("4. Return to previous menu")

        # take user input
        userChoice = input("Choose and option with '1', through '4': ")

        if userChoice == '1':
            lName = input("Enter the last name of the user you want to search for: ")
            # searches for users with inputted last name in system and adds them to searchList
            for username in ALL_STUDENT_ACCOUNTS:
                if lName == ALL_STUDENT_ACCOUNTS[username]['lastName']:
                    searchList.append(username)
            # true if searchList is empty
            if not searchList:
                print("No one was found with that last name")
            else:
                # print each found user and enumerate searchList so user can input number to send request
                for index, username in enumerate(searchList):
                    last_name = ALL_STUDENT_ACCOUNTS[username]['lastName']
                    first_name = ALL_STUDENT_ACCOUNTS[username]['firstName']
                    university = ALL_STUDENT_ACCOUNTS[username]['university']
                    major = ALL_STUDENT_ACCOUNTS[username]['major']
                    # print first and last name as well as university and major
                    print(f'{index}. {first_name} {last_name}, {university}, {major}')

                print("Enter the number of a person to send a friend request, or enter anything else to exit")
                friendChoice = input("Enter here: ")


                # check if friendChoice is a digit in the range of shown users
                if friendChoice.isdigit() and int(friendChoice) in range(0, len(searchList)):
                    # set index to int version of friendChoice and use as index to look in list
                    index = int(friendChoice)
                    # sets receivingUser to the username stored in searchList and add to users friend request list
                    receivingUser = searchList[index]
                    ALL_STUDENT_ACCOUNTS[receivingUser]['requests'].append(globalUsername)
                else:
                    return


        elif userChoice == '2':
            University = input("Enter the University of the user you want to search for: ")
            for username in ALL_STUDENT_ACCOUNTS:
                if University == ALL_STUDENT_ACCOUNTS[username]['university']:
                    searchList.append(username)

            if not searchList:
                print("No one was found in that university")
            else:
                # print each found user
                for index, username in enumerate(searchList):
                    last_name = ALL_STUDENT_ACCOUNTS[username]['lastName']
                    first_name = ALL_STUDENT_ACCOUNTS[username]['firstName']
                    university = ALL_STUDENT_ACCOUNTS[username]['university']
                    major = ALL_STUDENT_ACCOUNTS[username]['major']
                    print(f'{index}. {first_name} {last_name}, {university}, {major}')

                print("Enter the number of a person to send a friend request, or enter anything else to exit")
                friendChoice = input("Enter here: ")


               # check if friendChoice is a digit in the range of shown users
                if friendChoice.isdigit() and int(friendChoice) in range(0, len(searchList)):
                    # set index to int version of friendChoice and use as index to look in list
                    index = int(friendChoice)
                    # sets receivingUser to the username stored in searchList and add to users friend request list
                    receivingUser = searchList[index]
                    ALL_STUDENT_ACCOUNTS[receivingUser]['requests'].append(globalUsername)
                else:
                    return
        elif userChoice == '3':
            Major = input("Enter the Major of the user you want to search for: ")
            for username in ALL_STUDENT_ACCOUNTS:
                if Major == ALL_STUDENT_ACCOUNTS[username]['major']:
                    searchList.append(username)

            if not searchList:
                print("No one was found with that major")
            else:
                # print each found user
                for index, username in enumerate(searchList):
                    last_name = ALL_STUDENT_ACCOUNTS[username]['lastName']
                    first_name = ALL_STUDENT_ACCOUNTS[username]['firstName']
                    university = ALL_STUDENT_ACCOUNTS[username]['university']
                    major = ALL_STUDENT_ACCOUNTS[username]['major']
                    print(f'{index}. {first_name} {last_name}, {university}, {major}')

                print("Enter the number of a person to send a friend request, or enter anything else to exit")
                friendChoice = input("Enter here: ")

                # check if friendChoice is a digit in the range of shown users
                if friendChoice.isdigit() and int(friendChoice) in range(0, len(searchList) - 1):
                    # set index to int version of friendChoice and use as index to look in list
                    index = int(friendChoice)
                    # sets receivingUser to the username stored in searchList and add to users friend request list
                    receivingUser = searchList[index]
                    ALL_STUDENT_ACCOUNTS[receivingUser]['requests'].append(globalUsername)
                else:
                    return
        elif userChoice == '4':
            return
        else:
            print("Invalid, please choose an option with '1', through '4'")
            find()


# Important links function
def importantLinks():
    print("1. A Copyright Notice")
    print("2. About")
    print("3. Accessibility")
    print("4. User Agreement")
    print("5. Privacy Policy")
    print("6. Cookie Policy")
    print("7. Copyright Policy")
    print("8. Brand Policy")
    print("9. return to previous menu")
    # only display option 10 if user is logged in
    if globalUsername is not None:
        print("10. Languages")

    # user input to choose option
    if globalUsername is None:
        userChoice = input("Select an option with '1' through '9': ")
    else:
        userChoice = input("Select an option with '1' through '10': ")

    # menu for important links
    if userChoice == '1':
        print("InCollege © copyright-2023")
        importantLinks()
    elif userChoice == '2':
        print("InCollege aims to help students connect with each other and find jobs")
        importantLinks()
    elif userChoice == '3':
        print("InCollege works to ensure easy access to all users")
        importantLinks()
    elif userChoice == '4':
        print("By creating an account with InCollege, you automatically agree to our terms and services")
        importantLinks()
    elif userChoice == '5':
        print("InCollege ensures that user data will not be disclosed to unauthorized parties")

        # check if user is logged in using global variable in order to allow logged in user to change privacy settings
        if globalUsername is not None:
            privacyChange()
        importantLinks()
    elif userChoice == '6':
        print("We use cookies to enhance our overall user experience")
        importantLinks()
    elif userChoice == '7':
        print("We Reserve the right to use the InCollege © name and logo")
        importantLinks()
    elif userChoice == '8':
        print("Our brand policy is to ensure easy access to work opportunities to all students")
        importantLinks()
    elif userChoice == '9':
        return

    # allows logged in users to change language
    elif globalUsername is not None and userChoice == '10':
        languageChange()
        importantLinks()
    # if and elif statements change range of input based on logged in or not logged in user
    else:
        if globalUsername is None:
            print("Invalid. Please choose an option with '1' through '9'")

        elif globalUsername is not None:
            print("Invalid. Please choose an option with '1' through '10'")
    importantLinks()


# function to change language
def languageChange():
    print("1. Set language to English")
    print("2. Set Language to Spanish")
    print("3. Return to previous menu")
    languageChoice = input("Choose an option with '1' or '2': ")

    if languageChoice == '1':
        # updates 'Language' value in ALL_STUDENT_ACCOUNTS to 'English'
        ALL_STUDENT_ACCOUNTS[globalUsername]['Language'] = 'English'
        print("Language set to English")
        languageChange()
    elif languageChoice == '2':
        # updates 'Language' value in ALL_STUDENT_ACCOUNTS to 'Spanish'
        ALL_STUDENT_ACCOUNTS[globalUsername]['Language'] = 'Spanish'
        print("Language set to Spanish")
        languageChange()
    else:
        return


# function for changing privacy options
def privacyChange():
    print("1. Turn on InCollege Email")
    print("2. Turn off InCollege Email")
    print("3. Turn on SMS")
    print("4. Turn off SMS")
    print("5. Turn on Targeted Advertising Features")
    print("6. Turn off Targeted Advertising Features")
    print("7. return to previous")

    # user input for privacy options
    privacyChoice = input("Select an option with '1' through '7': ")
    if privacyChoice == '1':
        # sets 'Email' in ALL_STUDENT_ACCOUNTS to True
        ALL_STUDENT_ACCOUNTS[globalUsername]['Email'] = True
        print("Email turned on")
        privacyChange()
    elif privacyChoice == '2':
        # sets 'Email' in ALL_STUDENT_ACCOUNTS to False
        ALL_STUDENT_ACCOUNTS[globalUsername]['Email'] = False
        print("Email turned off")
        privacyChange()
    elif privacyChoice == '3':
        # sets 'SMS' in ALL_STUDENT_ACCOUNTS to True
        ALL_STUDENT_ACCOUNTS[globalUsername]['SMS'] = True
        print("SMS turned on")
        privacyChange()
    elif privacyChoice == '4':
        # sets 'SMS' in ALL_STUDENT_ACCOUNTS to False
        ALL_STUDENT_ACCOUNTS[globalUsername]['SMS'] = False
        print("SMS turned off")
        privacyChange()
    elif privacyChoice == '5':
        # sets 'Advertising' in ALL_STUDENT_ACCOUNTS to True
        ALL_STUDENT_ACCOUNTS[globalUsername]['Advertising'] = True
        print("Targeted Advertising turned on")
        privacyChange()
    elif privacyChoice == '6':
        # sets 'Advertising' in ALL_STUDENT_ACCOUNTS to False
        ALL_STUDENT_ACCOUNTS[globalUsername]['Advertising'] = False
        print("Targeted Advertising turned off")
        privacyChange()
    elif privacyChoice == '7':
        return
    else:
        print("Invalid, please choose an option with '1' through '7'")
        privacyChange()


# useful links function
def usefulLinks():
    print("1. General")
    print("2. Browse InCollege")
    print("3. Business Solutions")
    print("4. Directories")
    print("5. Return to previous menu")

    # user input to choose option
    userChoice = input("Select an option with '1' through '5': ")

    # menu for useful links options
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
        print("Invalid. Please choose an option with '1' through '5'")
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
    # only show option 8 if user is not signed in
    if globalUsername is None:
        print("8. Sign up")

    # user input to choose options 1-8 if not signed in, or 1-7 if signed in
    if globalUsername is None:
        userChoice = input("Select an option with '1' through '8': ")

    else:
        userChoice = input("Select an option with '1' through '7': ")

    # menu for general options
    if userChoice == '1':
        print("We're here to help")
        generalMenu()
    elif userChoice == '2':
        print("In College: Welcome to In College, the world's largest college student"
              "network with many users in many countries and territories worldwide")
        generalMenu()
    elif userChoice == '3':
        print("In College Pressroom: Stay on top of the latest news, updates, and reports")
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
    # allows user to login or create account only if not logged in
    elif globalUsername is None and userChoice == '8':
        print("1. Login")
        print("2. Create a new account")
        loginChoice = input("Choose an option with '1' or '2': ")
        if loginChoice == '1':
            # sets variable username to return value of login()
            username = login()
            # sends user to loggedinScreen with username as parameter if username is non empty
            if username is not None:
                loggedinScreen(username)
            initialScreen()
        # create account
        elif loginChoice == '2':
            # check if account limit reached
            if len(ALL_STUDENT_ACCOUNTS) >= 10:
                print("Sorry, all permitted accounts have been created. Please come back later.\n")
                initialScreen()
            else:
                username = createAccount()
                loggedinScreen(username)
                initialScreen()
    else:
        # uses globalUsername to display different options if logged in or not
        if globalUsername is not None:
            print("Invalid. Please choose an option with '1' through '7'")
        if globalUsername is None:
            print("Invalid. Please choose an option with '1' through '8'")
        generalMenu()


# show my network function
def showMyNetwork():
    print("1. View friend requests")
    print("2. Show friends")
    print("3. Return to previous menu")

    userChoice = input("Select an option with '1', '2', or '3': ")

    if userChoice == '1':
        # search for each friend request
        for requester in ALL_STUDENT_ACCOUNTS[globalUsername]['requests']:
            # set first, last name and unoversity of requester to various variables
            requester_firstName = ALL_STUDENT_ACCOUNTS[requester]['firstName']
            requester_lastName = ALL_STUDENT_ACCOUNTS[requester]['lastName']
            requester_university = ALL_STUDENT_ACCOUNTS[requester]['university']
            # print details of friend request
            print(f'{requester_firstName} {requester_lastName} from {requester_university} has sent you a friend request')

            requestChoice = input("Enter 1 to accept the request or 2 to deny: ")
            while requestChoice != '1' or requestChoice != '2':
                requestChoice = input("Invalid input, Enter 1 to accept the request or 2 to deny: ")

            if requestChoice == '1':
                # add requester to the current users list of friends
                ALL_STUDENT_ACCOUNTS[globalUsername]['friends'].append(requester)
                # remove requester from list of friend requests
                ALL_STUDENT_ACCOUNTS[globalUsername]['requests'].remove(requester)
                # add current user to requesters friend list
                ALL_STUDENT_ACCOUNTS[requester]['friends'].append(globalUsername)
                print(f'You have successfully added {requester_firstName} as a friend!')

            elif requestChoice == '2':
                # only remove requester from list of friend requests
                ALL_STUDENT_ACCOUNTS[globalUsername]['requests'].remove(requester)
                print(f'You have denied a friend request from {requester_firstName}')
        showMyNetwork()


    elif userChoice == '2':
        # create list to add friends into
        friendList = []

        for friend in ALL_STUDENT_ACCOUNTS[globalUsername]['friends']:
                friendList.append(friend)
            # true if friendList is empty
        if not friendList:
            print("You have not added any friends yet")
        else:
            friendChoice = ''
            while friendChoice != 'exit':
                # print each found user and enumerate searchList so user can input number to send request
                for index, username in enumerate(friendList):
                    last_name = ALL_STUDENT_ACCOUNTS[username]['lastName']
                    first_name = ALL_STUDENT_ACCOUNTS[username]['firstName']
                    university = ALL_STUDENT_ACCOUNTS[username]['university']
                    major = ALL_STUDENT_ACCOUNTS[username]['major']
                    # print first and last name as well as university and major
                    print(f'{index}. {first_name} {last_name}, {university}, {major}')

                print("Enter the number of a friend to disconnect from them, or type exit to leave")
                friendChoice = input("Enter here: ")

                # check if friendChoice is a digit in the range of shown users
                if friendChoice.isdigit() and friendChoice in range(0, len(friendList) - 1):
                    # set index to int version of friendChoice and use as index to look in list
                    index = int(friendChoice)
                    # sets disconnectedUser to username of selected friend
                    disconnectedUser = friendList[index][1]
                    ALL_STUDENT_ACCOUNTS[globalUsername]['friends'].remove(disconnectedUser)
                    ALL_STUDENT_ACCOUNTS[disconnectedUser]['friends'].remove(globalUsername)
        showMyNetwork()

    elif userChoice == '3':
        return
    else:
        print("Invalid Input, Select an option with '1', '2', or '3'")
        showMyNetwork()






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


# function for the marketing before the user login
def preLoggedInScreen():
    print("Success story: Congratulations!!! A USF student has successfully landed an "
    "internship for the Summer 2024 with the help of InCollege!\n")
    print("Select one of the following options:")
    print("1. Find out why you would want to join InCollege")
    print("2. Find out who has joined InCollege")
    print("3. Login into your account")
    print("4. Return to the previous screen")

    userChoice = input("Select an option with '1', '2', '3', or '4': ")

    if userChoice == "1":
        print("Video is now playing")
    elif userChoice == "2":
        find()
        preLoggedInScreen()
    elif userChoice == "3":
        # sets variable username to return value of login()
        username = login()
        # sends user to loggedinScreen with username as parameter if username is non empty
        if username is not None:
            loggedinScreen(username)
            preLoggedInScreen()
    elif userChoice == "4":
        return
    else:
        print("Invalid. Please select one of the following options: '1', '2', '3', or '4'.\n")
        preLoggedInScreen()


# function for when the user is logged in
def loggedinScreen(username):
    # set isLoggedIn Boolean to true
    globalUsername = username

    if ALL_STUDENT_ACCOUNTS[username]['requests'] is not None:
        print("\nYou have pending friend requests! Go to Show my network to view")
    # other submenu would go here
    print(" ")
    print("1. Search for a job")
    print("2. Find someone you know")
    print("3. Learn a new skill")
    print("4. View Useful Links")
    print("5. View InCollege Important Links")
    print("6. Show my network")
    print("7. log out")

    # User choose an option
    userChoice = input("Select an option with '1', through '7': ")

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
        showMyNetwork()
        loggedinScreen(username)
    elif userChoice == '7':
        print("\nYou have successfully logged out\n")
        globalUsername = None
        return
    else:
        print("Invalid. Please choose a valid option of either '1', '2', or '3'.\n")
        loggedinScreen()


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
        preLoggedInScreen()
        initialScreen()
    # create account
    elif userChoice == '2':
        # check if account limit reached
        if len(ALL_STUDENT_ACCOUNTS) >= 10:
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
