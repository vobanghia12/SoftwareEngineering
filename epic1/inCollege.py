'''
Team Wyoming
Fall '23
'''

# dictionary with key as username password as the value
ALL_STUDENT_ACCOUNTS = {}
ALL_JOBS = {}
ALL_PROFILES = {}
MESSAGES = {}

#dictionary to store applicants and the applied job which has been deleted
ALL_APPLICANT_DELETED_JOBS = set()

# global variable to track current user (also used to check if user is logged in or not)
globalUsername = None

searchList = []

friendList = []

numberOfDays = 0

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
    while not firstName:
        firstName = input("Invalid, Enter your first name: ")

    # input last name and force re-input while empty
    lastName = input("Enter your last name: ")
    while not lastName:
        lastName = input("Invalid, Enter your last name: ")

    # input university and force re-input while empty
    university = input("Enter your university: ")
    while not university:
        university = input("Invalid, Enter your university: ")

    # input major and force re-input while empty
    major = input("Enter your major: ")
    while not major:
        major = input("Invalid, Enter your major: ")

    # Add a choice for membership tier during signup
    print("Choose your membership tier:")
    print("1. Standard (Free)")
    print("2. Plus ($10/month)")
    membership_choice = input("Enter '1' for Standard or '2' for Plus: ")

    if membership_choice == '1':
        membership_tier = 'Standard'
        billing_status = 'Free'  # No billing for Standard members
    elif membership_choice == '2':
        membership_tier = 'Plus'
        billing_status = 'Active'  # Plus members are billed $10/month
        # Implement billing logic here to charge $10 from the student's account

    # keep track of current number of jobs posted and users for notifications
    numUsers = 0
    numJobs = 0
    for job in ALL_JOBS:
        numJobs += 1

    for user in ALL_STUDENT_ACCOUNTS:
        numUsers += 1


    # Key is the username, values are password, firstName, lastName, university, major, Language
    # also holds booleans for SMS, Email and Advertising, as well as lists for friends and friend requests
    # numJobs and numUsers are personal trackers to help display notifications of new jobs and users
    ALL_STUDENT_ACCOUNTS[username] = {
        'password': password,
        'firstName': firstName,
        'lastName': lastName,
        'university': university,
        'major': major,
        'membership_tier': membership_tier,
        'billing_status': billing_status,
        'Language': 'English',
        'SMS': True,
        'Email': True,
        'Advertising': True,
        'friends': [],
        'requests': [],
        'numJobs': numJobs,
        'numUsers': numUsers,
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

    if len(ALL_JOBS) >= 10: #Increase the number of jobs listing supported
        print("Sorry, all permitted jobs have been created. Please come back later.\n")
        return
    else:
        # creates job with all attributes defined above
        ALL_JOBS[title] = {
            'description': description,
            'employer': employer,
            'location': location,
            'salary': salary,
            'poster': poster,
            'applicants': set(), # add applicants attributes to track job's applicants
            'applications': set(), # add applications
            'saved': False # add saved attribute to track if job is saved
        }
        print("You have successfully posted a job!")
        return

def applyJob():
    #print the titles of all jobs
    for title in ALL_JOBS:
        print(title)
    #prompt the user to choose a job
    jobTitle = input("Enter the title of the job you want to apply to: ")
    #check if the job title is valid, or if the job is already applied to, or if the user is the poster
    if jobTitle not in ALL_JOBS:
        print("Invalid job title")
        return
    elif globalUsername in ALL_JOBS[jobTitle]['applicants']:
        print("You have already applied to this job")
        return
    elif globalUsername == ALL_JOBS[jobTitle]['poster']:
        print("You cannot apply to a job you posted")
        return
    else:
        #add the user to the job's applicants
        ALL_JOBS[jobTitle]['applicants'].add(globalUsername)

        #Ask the user to enter a graduation date, a date they can start working, and a paragraph explaining why they are a good fit for the job, and store this application to the job
        graduationDate = input("Enter your graduation date: ")
        startDate = input("Enter a date you can start working: ")
        paragraph = input("Enter a paragraph explaining why you are a good fit for the job: ")
        ALL_JOBS[jobTitle]['applications'].add((globalUsername, graduationDate, startDate, paragraph))
        print("You have successfully applied to the job")
        global numberOfDays
        numberOfDays = 0
        return

def saveJob():
    #print the titles of all jobs and its saved status
    for title in ALL_JOBS:
        saved = ALL_JOBS[title]['saved']
        if saved == True:
            print(title, "Saved")
        else:
            print(title, "Not Saved")

    #prompt the user to choose a job
    jobTitle = input("Enter the title of the job you want to save/unsave: ")
    #check if the job title is valid
    if jobTitle not in ALL_JOBS:
        print("Invalid job title")
        return
    else:
        #if the job is saved, unsave it
        if ALL_JOBS[jobTitle]['saved'] == True:
            ALL_JOBS[jobTitle]['saved'] = False
            print("You have successfully unsaved the job")
            return
        #if the job is not saved, save it
        elif ALL_JOBS[jobTitle]['saved'] == False:
            ALL_JOBS[jobTitle]['saved'] = True
            print("You have successfully saved the job")
            return

#Func to handle job titles listing
def listingSearch():
    print("1. List all posted jobs")
    print("2. List of all jobs applied to")
    print("3. List of all jobs not applied to")
    print("4. List of saved jobs")
    print("5. Apply for a job")
    print("6. Save/Unsave a job")
    print("7. Return to previous menu")

    # user input to choose option
    userChoice = input("Select an option with '1', '2', '3', '4', '5', '6', or '7': ")

    # menu for listing search options
    if userChoice == '1':
        # check if there are any jobs posted
        if len(ALL_JOBS) == 0:
            print("No jobs have been posted yet")
            listingSearch()
        else:
            # print each job (title, description, employer, location, salary) and indicate if applicant has applied or not
            for title in ALL_JOBS:
                description = ALL_JOBS[title]['description']
                employer = ALL_JOBS[title]['employer']
                location = ALL_JOBS[title]['location']
                salary = ALL_JOBS[title]['salary']
                poster = ALL_JOBS[title]['poster']
                applicants = ALL_JOBS[title]['applicants']
                if globalUsername in applicants:
                    print(f'{title}, {description}, {employer}, {location}, {salary}, {poster}, Applied')
                else:
                    print(f'{title}, {description}, {employer}, {location}, {salary}, {poster}, Not Applied')

            #prompt the user for applying for job or saving job
            apply = input("Select '1' if you want to apply for a job, '2' to save/unsave a job, or anything else to exit")
            if apply == "1":
                applyJob()
                listingSearch()
            elif apply == "2":
                saveJob()
                listingSearch()
            else:
                listingSearch()

    elif userChoice == '2':
        #List all the job this applicant have applied
        for title in ALL_JOBS:
            applicants = ALL_JOBS[title]['applicants']
            if globalUsername in applicants:
                # print each job (title, description, employer, location, salary)
                description = ALL_JOBS[title]['description']
                employer = ALL_JOBS[title]['employer']
                location = ALL_JOBS[title]['location']
                salary = ALL_JOBS[title]['salary']

                print(f'{title}, {description}, {employer}, {location}, {salary}')

        #prompt the user for applying for job or saving job
        apply = input("Select '1' if you want to apply for a job, '2' to save/unsave a job, or anything else to exit")
        if apply == "1":
            applyJob()
            listingSearch()
        elif apply == "2":
            saveJob()
            listingSearch()
        else:
            listingSearch()

    elif userChoice == '3':
        #list all the jobs this applicant have not applied
        for title in ALL_JOBS:
            applicants = ALL_JOBS[title]['applicants']
            if globalUsername not in applicants:
                # print each job (title, description, employer, location, salary)
                description = ALL_JOBS[title]['description']
                employer = ALL_JOBS[title]['employer']
                location = ALL_JOBS[title]['location']
                salary = ALL_JOBS[title]['salary']

                print(f'{title}, {description}, {employer}, {location}, {salary}')

        #prompt the user for applying for job or saving job
        apply = input("Select '1' if you want to apply for a job, '2' to save/unsave a job, or anything else to exit")
        if apply == "1":
            applyJob()
            listingSearch()
        if apply == "2":
            saveJob()
            listingSearch()
        else:
            listingSearch()

    elif userChoice == '4':
        #List of saved jobs
        for title in ALL_JOBS:
            saved = ALL_JOBS[title]['saved']
            if saved == True:
                # print each job (title, description, employer, location, salary)
                description = ALL_JOBS[title]['description']
                employer = ALL_JOBS[title]['employer']
                location = ALL_JOBS[title]['location']
                salary = ALL_JOBS[title]['salary']

                print(f'{title}, {description}, {employer}, {location}, {salary}')

        #prompt the user for applying for job or saving job
        apply = input("Select '1' if you want to apply for a job, '2' to save/unsave a job, or anything else to exit")
        if apply == "1":
            applyJob()
            listingSearch()
        if apply == "2":
            saveJob()
            listingSearch()
        else:
            listingSearch()

    elif userChoice == '5':
        #Apply for a job
        applyJob()
        listingSearch()

    elif userChoice == '6':
        #Save/Unsave a job
        saveJob()
        listingSearch()

    elif userChoice == '7':
        #Return to previous menu
        return

    else:
        print("Invalid. Please choose an option with '1', '2', '3', '4', '5', or '6'.\n")
        listingSearch()


# Job search/Internship Option
def jobSearch():
    #notify the user if a job they have applied has been deleted
    if globalUsername in ALL_APPLICANT_DELETED_JOBS:
        print("A job you have applied to has been deleted")

    #checks how many jobs have been applied
    numberOfAppliedJobs = 0

    for title in ALL_JOBS:
        applicants = ALL_JOBS[title]['applicants']
        if globalUsername in applicants:
            numberOfAppliedJobs += 1

    if numberOfAppliedJobs == 0:
        print(f"You have currently applied for {numberOfAppliedJobs} jobs")

    print("1. Search for a job/internship")
    print("2. Post a job/internship")
    print("3. Return to main menu")


    # User choose an option
    userChoice = input("Select an option with '1', '2', or '3': ")

    # Option menu:
    if userChoice == '1':
        listingSearch()
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
                    print("request sent")
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
        print("InCollege Â© copyright-2023")
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
        print("We Reserve the right to use the InCollege Â© name and logo")
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
            print(f'{requester_firstName} {requester_lastName} '
                  f'from {requester_university} has sent you a friend request')

            requestChoice = input("Enter 1 to accept the request or 2 to deny: ")
            while requestChoice != '1' and requestChoice != '2':
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


# function to view friend's profiles
def viewFriendsProfiles():
    # create list to add friends into
    friendList = []



    for friend in ALL_STUDENT_ACCOUNTS[globalUsername]['friends']:
        friendList.append(friend)
    # true if friendList is empty

    if not friendList:
        print("You have not added any friends yet")
        return

    # if user has friends
    if friendList:
        # variable to keep track of number of friends
        num = 1
        for friend in friendList:
            # add friends first and last name to variable
            friend_name = ALL_STUDENT_ACCOUNTS[friend]['firstName'] + ' ' + ALL_STUDENT_ACCOUNTS[friend]['lastName']
            print(f'{num}. {friend_name}')
            num += 1

        # user input to choose a friend
        print("Enter the friends number to see their profile or press anything else to exit")
        viewChoice = input("Enter Here: ")
        # check if input is number and convert to int in index
        if viewChoice.isdigit():
            index = int(viewChoice)-1
            # check if index is in valid range
            if index >= 0 and index <= len(friendList):
                # variable to store friends name
                friend_username = friendList[index]
                if friend_username in ALL_PROFILES:
                    friend_name = ALL_STUDENT_ACCOUNTS[friend_username]['firstName'] + ' ' + \
                              ALL_STUDENT_ACCOUNTS[friend_username]['lastName']

                    print(f'{friend_name}\'s Profile:\n')

                    print(f"Title: {ALL_PROFILES[friend_username]['title']}")
                    print(f"Major: {ALL_PROFILES[friend_username]['major']}")
                    print(f"University: {ALL_PROFILES[friend_username]['university']}")
                    print(f"About: {ALL_PROFILES[friend_username]['about']}")
                    print(f"Education: {ALL_PROFILES[friend_username]['education']}")

                    # use for loop to print each job
                    for i in range(len(ALL_PROFILES[friend_username]['job_title'])):
                    # variable to store job number
                        x = i
                        n = i + 1
                        # Access and print the job attributes
                        print(f"Job number {n} Title: {ALL_PROFILES[friend_username]['job_title'][x]}")
                        print(f"Employer: {ALL_PROFILES[friend_username]['job_employer'][x]}")
                        print(f"Start Date: {ALL_PROFILES[friend_username]['job_date_start'][x]}")
                        print(f"End Date: {ALL_PROFILES[friend_username]['job_date_end'][x]}")
                        print(f"Location: {ALL_PROFILES[friend_username]['job_location'][x]}")
                        print(f"Description: {ALL_PROFILES[friend_username]['job_description'][x]}")
                        print("\n")


                elif friend_username not in ALL_PROFILES:
                    print("That friend has not made a profile yet")
                    viewFriendsProfiles()

                else:
                    print("Invalid Input")
                    viewFriendsProfiles()


# function to add a job to profile
def profileJobMenu():
    print("1. Add a job")
    print("2. Delete a job")
    print("3. Return to previous menu")

    userChoice = input("Choose an option with '1' through '3': ")

    if userChoice == '1':
        # checks if max number of jobs has been reached, then asks for input to appends to each job attribute
        if len(ALL_PROFILES[globalUsername]['job_title']) < 3:
            job_title = input("Enter the title of your job: ")
            ALL_PROFILES[globalUsername]['job_title'].append(job_title)
            job_employer = input("Enter the name of your employer: ")
            ALL_PROFILES[globalUsername]['job_employer'].append(job_employer)
            job_date_start = input("Enter the start date of your job: ")
            ALL_PROFILES[globalUsername]['job_date_start'].append(job_date_start)
            job_date_end = input("Enter the end date of your job: ")
            ALL_PROFILES[globalUsername]['job_date_end'].append(job_date_end)
            job_location = input("Enter the location of your job: ")
            ALL_PROFILES[globalUsername]['job_location'].append(job_location)
            job_description = input("Enter a description of your job: ")
            ALL_PROFILES[globalUsername]['job_description'].append(job_description)

        else:
            print("You have already inserted the max amount of job experiences")
        profileJobMenu()

    elif userChoice == '2':
        for i in range(len(ALL_PROFILES[globalUsername]['job_title'])):
            # variable to store job number
            n = i + 1
            # Access and print the job attributes
            print(f"Job number {n} Title: {ALL_PROFILES[globalUsername]['job_title'][i]}")
        jobChoice = input("Enter the number of a job to delete: ")

        if jobChoice == '1':
            ALL_PROFILES[globalUsername]['job_title'].pop(0)
            ALL_PROFILES[globalUsername]['job_employer'].pop(0)
            ALL_PROFILES[globalUsername]['job_date_start'].pop(0)
            ALL_PROFILES[globalUsername]['job_date_end'].pop(0)
            ALL_PROFILES[globalUsername]['job_location'].pop(0)
            ALL_PROFILES[globalUsername]['job_description'].pop(0)
        elif jobChoice == '2':
            ALL_PROFILES[globalUsername]['job_title'].pop(1)
            ALL_PROFILES[globalUsername]['job_employer'].pop(1)
            ALL_PROFILES[globalUsername]['job_date_start'].pop(1)
            ALL_PROFILES[globalUsername]['job_date_end'].pop(1)
            ALL_PROFILES[globalUsername]['job_location'].pop(1)
            ALL_PROFILES[globalUsername]['job_description'].pop(1)
        elif jobChoice == '3':
            ALL_PROFILES[globalUsername]['job_title'].pop(2)
            ALL_PROFILES[globalUsername]['job_employer'].pop(2)
            ALL_PROFILES[globalUsername]['job_date_start'].pop(2)
            ALL_PROFILES[globalUsername]['job_date_end'].pop(2)
            ALL_PROFILES[globalUsername]['job_location'].pop(2)
            ALL_PROFILES[globalUsername]['job_description'].pop(2)
        else:
            print("Invalid Input")
            profileJobMenu()
        profileJobMenu()


# function to change profile
def profileChange():
    # checks if profile already started in ALL_PROFILES
    if globalUsername not in ALL_PROFILES:

        # various statements to input job info
        title = input("Enter a title: ")
        major = input("Enter a Major: ")
        while not major:
            major = input("Error, major cant be empty, Enter a Major: ")
        major = major.title()
        university = input("Enter a university: ")
        while not university:
            university = input("Error, university cant be empty, Enter a university: ")
        university = university.title()
        about = input("Enter data for your about page: ")
        education = input("Enter your Education: ")
        while not education:
            education = input("Error, education cant be empty, Enter your Education: ")

        # add all info to dictionary
        ALL_PROFILES[globalUsername] = {
            'title': title,
            'major': major,
            'university': university,
            'about': about,
            'education': education,
            'job_title': [],
            'job_employer': [],
            'job_date_start': [],
            'job_date_end': [],
            'job_location': [],
            'job_description': [],
        }
        # recall function to get sent to menu below
        profileChange()

    # sends to below menu if profile already started
    elif globalUsername in ALL_PROFILES:
        print("1. Title")
        print("2. Major")
        print("3. University")
        print("4. About")
        print("5. Experience")
        print("6. Education")
        print("7. View your profile")
        print("8. Return to previous menu")

        userChoice = input("Select the part of your profile you would like to change with '1' through '7': ")

        if userChoice == '1':
            title = input("Enter a new title: ")
            ALL_PROFILES[globalUsername]['title'] = title
            profileChange()
        elif userChoice == '2':
            major = input("Enter a new major: ")
            while not major:
                major = input("Error, major cant be empty, Enter a Major: ")
                major = major.title()
            ALL_PROFILES[globalUsername]['major'] = major
            print("You successfuly changed your major!")
            profileChange()
        elif userChoice == '3':
            university = input("Enter a new university: ")
            while not university:
                university = input("Error, university cant be empty, Enter a university: ")
                university = university.title()
            ALL_PROFILES[globalUsername]['university'] = university
            print("You successfuly changed your university!")
            profileChange()
        elif userChoice == '4':
            about = input("Enter new data for your About Page: ")
            ALL_PROFILES[globalUsername]['about'] = about
            print("You successfuly changed your about section!")
            profileChange()
        elif userChoice == '5':
            # calls menu to add / delete jobs
            profileJobMenu()
        elif userChoice == '6':
            education = input("Enter new Education details: ")
            while not education:
                education = input("Error, education cant be empty, Enter your Education: ")
            ALL_PROFILES[globalUsername]['education'] = education
            profileChange()
        elif userChoice == '7':
            # access first and last name to print
            first_name = ALL_STUDENT_ACCOUNTS[globalUsername]['firstName']
            last_name = ALL_STUDENT_ACCOUNTS[globalUsername]['lastName']

            # print first and last name as well as rest of profile
            print(f'{first_name} {last_name}\'s Profile:\n')

            print(f"Title: {ALL_PROFILES[globalUsername]['title']} ")
            print(f"Major: {ALL_PROFILES[globalUsername]['major']}")
            print(f"University: {ALL_PROFILES[globalUsername]['university']}")
            print(f"About: {ALL_PROFILES[globalUsername]['about']}")
            print(f"Education: {ALL_PROFILES[globalUsername]['education']}")

            # use for loop to print each job
            for i in range(len(ALL_PROFILES[globalUsername]['job_title'])):

                # variable to store job number
                n = i + 1
                # Access and print the job attributes
                print(f"Job number {n} Title: {ALL_PROFILES[globalUsername]['job_title'][i]}")
                print(f"Employer: {ALL_PROFILES[globalUsername]['job_employer'][i]}")
                print(f"Start Date: {ALL_PROFILES[globalUsername]['job_date_start'][i]}")
                print(f"End Date: {ALL_PROFILES[globalUsername]['job_date_end'][i]}")
                print(f"Location: {ALL_PROFILES[globalUsername]['job_location'][i]}")
                print(f"Description: {ALL_PROFILES[globalUsername]['job_description'][i]}")
                print("\n")

        elif userChoice == '8':
            return
        else:
            print("Invalid, Select an option with '1' through '7'")
            profileChange()


# function to display profile menu
def profileMenu():
    print("1. View Friends profiles")
    print("2. Edit/view your profile")
    print("3. return to previous menu")

    userChoice = input("Select an option with '1' through '3': ")

    if userChoice == '1':
        viewFriendsProfiles()
        profileMenu()
    elif userChoice == '2':
        profileChange()
        profileMenu()
    elif userChoice == '3':
        return
    else:
        print("Invalid, Select an option with '1' through '3'")


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


def deleteJob(username):
    jobs_to_be_deleted = []

    #check if this username is the poster of any jobs
    if not ALL_JOBS:
        print("No jobs to delete.")
        return

    for title in ALL_JOBS:
        if ALL_JOBS[title]['poster'] == username:
            has_posted_jobs = 0
            break

    if has_posted_jobs == 1:
        print("You have not posted any jobs")
        return


    #print all the jobs that the user is the poster
    for title in ALL_JOBS:
        jobs_to_be_deleted.append(title)

    i = 0
    for jobs in jobs_to_be_deleted:
        print(f"{i+1}.", jobs)
        i += 1

    #ask the user which job they want to delete
    jobChoice = input("Enter the job you want to delete: ")

    if jobChoice in jobs_to_be_deleted:
        job_in_array = 0

    if job_in_array == 0:
        ALL_APPLICANT_DELETED_JOBS.update(ALL_JOBS[jobChoice]['applicants'])

        del ALL_JOBS[jobChoice]
        print("Job deleted")
        return
    else:
        print("Invalid input")
        deleteJob(username) #delete the job

    #check if the input is a number
    if jobChoice.isdigit():
        #check if the input is in the range of the list
        if int(jobChoice) in range(1, len(ALL_JOBS)+1):
            #store applicants of this job so that they can be notified later when they are in the job section
            ALL_APPLICANT_DELETED_JOBS.update(ALL_JOBS[int(jobChoice)-1]['applicants'])

            #delete the job
            ALL_JOBS.pop(int(jobChoice)-1)
            print("Job deleted")
        else:
            print("Invalid input")
            deleteJob(username) #delete the job

    else:
        print("Invalid input")
        deleteJob(username)
    return

def sendMessage(username):
    friendList = []

    print("Here are a list of friends you can message: \n")
    for friend in ALL_STUDENT_ACCOUNTS[globalUsername]['friends']:
        friendList.append(friend)

    #printing out friends
    for username in friendList:
        last_name = ALL_STUDENT_ACCOUNTS[username]['lastName']
        first_name = ALL_STUDENT_ACCOUNTS[username]['firstName']
        print(f"{first_name} {last_name}'s username: {username}")

    sendToUser = input("Enter the username you want to send a message to or type 'exit' to go back: ")
    if sendToUser not in ALL_STUDENT_ACCOUNTS[globalUsername]['friends']:
        print("I'm sorry, you are not friends with that person\n")
        sendMessage(username)
    elif sendToUser == "exit":
        return
    elif sendToUser in ALL_STUDENT_ACCOUNTS[globalUsername]['friends']:
        message = input("Enter the message you would like to send: \n")
        MESSAGES[sendToUser] = {
            'inbox': {
            'sender': username,
            'read': False,
            'message': message,
            }
        }
        print("Message sent\n")
        return
    else:
        print("Invalid input try again\n")
        sendMessage(username)

def viewInbox(username):
    for inbox in MESSAGES[username]['inbox']:
        if inbox['read'] == False:
            print("Here is a message your friend sent you: \n")
            print(inbox['message'])
            inbox['read'] = True
            print("\n")
            sendChoice = input("Do you want to respond? (y/n)").lower()
            if sendChoice == 'y':
                message = input("Enter the message you would like to send: \n")
                sendToUser = inbox['sender']
                MESSAGES[sendToUser] = {
                      'inbox':
                    {
                        'sender': username,
                        'read': False,
                        'message': message,
                    }
                }
                print("Message sent\n")
            deleteChoice = input("Do you want to delete this message? (y/n)").lower()
            if deleteChoice == 'y':
                del MESSAGES[username]['inbox']
                print("Message deleted\n")
    return

def messagePlus(username): #function for plus member messaging
    #check if the user is a plus member
    if ALL_STUDENT_ACCOUNTS[username]['membership_tier'] != 'Plus':
        print("You are not a plus member, you cannot message people\n")
        return

    friendList = []

    #get the list of all of the students who are in the system
    for student in ALL_STUDENT_ACCOUNTS:
        friendList.append(student)

    #printing out friends
    for username in friendList:
        last_name = ALL_STUDENT_ACCOUNTS[username]['lastName']
        first_name = ALL_STUDENT_ACCOUNTS[username]['firstName']
        print(f"{first_name} {last_name}'s username: {username}")

    sendToUser = input("Enter the username you want to send a message to or type 'exit' to go back: ")

    #plus members can message anyone
    if sendToUser == "exit":
        return
    elif sendToUser in friendList:
        message = input("Enter the message you would like to send: \n")
        MESSAGES[sendToUser] = {
            'inbox': {
            'sender': username,
            'read': False,
            'message': message,
            }
        }
        print("Message sent\n")
        return
    else:
        print("Invalid input try again\n")
        messagePlus(username)

def notification(username):
     #notifications
    if numberOfDays > 7:
        print("Remember - you're going to want to have a job when you graduate. Make sure that you start to apply for jobs today!\n")
    if ALL_STUDENT_ACCOUNTS[username]['requests'] is not None:
        print("You have pending friend requests! Go to Show my network to view\n")
    if username not in ALL_PROFILES.keys():
        print("Don't forget to create a profile\n")
    if username not in MESSAGES.keys():
        print("\nYou have messages waiting for you")


# function for when the user is logged in
def loggedinScreen(username):

    global numberOfDays
    # set isLoggedIn Boolean to true
    global globalUsername 
    globalUsername = username

    #notifications
    notification(username)
    if globalUsername in ALL_APPLICANT_DELETED_JOBS:
        for job in ALL_APPLICANT_DELETED_JOBS.keys():
            if globalUsername in ALL_APPLICANT_DELETED_JOBS[job]:
                print(f"The job: {job} that you applied for has been deleted")
    if len(ALL_JOBS) > ALL_STUDENT_ACCOUNTS[username]['numJobs']:
        new_job = list(ALL_JOBS)[-1]
        print(f"A new job: {new_job} has been posted")
        ALL_STUDENT_ACCOUNTS[username]['numJobs'] = len(ALL_JOBS)
    if len(ALL_STUDENT_ACCOUNTS) > ALL_STUDENT_ACCOUNTS[username]['numUsers']:
        numNewUsers = len(ALL_STUDENT_ACCOUNTS) - ALL_STUDENT_ACCOUNTS[username]['numUsers']
        newUsers = list(ALL_STUDENT_ACCOUNTS.keys())[-numNewUsers:]
        for user in newUsers:
            print(f"{ALL_STUDENT_ACCOUNTS[user]['firstName']} has joined inCollege!")
        ALL_STUDENT_ACCOUNTS[username]['numUsers'] = len(ALL_STUDENT_ACCOUNTS)


    # other submenu would go here
    print(" ")
    print("1. Search for a job")
    print("2. Find someone you know")
    print("3. Learn a new skill")
    print("4. View Useful Links")
    print("5. View InCollege Important Links")
    print("6. Show my network")
    print("7. View/Edit profiles")
    print("8. Delete a job")
    print("9. log out")
    print("10. Message Friends")
    print("11. View Inbox")
    print("12. Message (Plus account only)")

    # User choose an option
    userChoice = input("Select an option with '1', through '12': ")

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
        profileMenu()
        loggedinScreen(username)
    elif userChoice == '8':
        deleteJob(username)
        loggedinScreen(username)
    elif userChoice == '9':
        print("\nYou have successfully logged out\n")
        # when they log off assume a day has passed
        numberOfDays += 1
        globalUsername = None
        return
    elif userChoice == '10':
        sendMessage(username)
        loggedinScreen(username)
    elif userChoice == '11':
        viewInbox(username)
        loggedinScreen(username)
    elif userChoice == '12':
        messagePlus(username)
        loggedinScreen(username)
    else:
        print("Invalid. Please choose a valid option of either '1', through '12'.\n")
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

