import unittest
import io
from inCollege import *
from contextlib import redirect_stdout
from io import StringIO
import mock
from unittest.mock import patch
import inCollege

#test showmynetwork() and find() function

class TestInCollege(unittest.TestCase):
    #test user in the system when not logged in
    @patch('inCollege.globalUsername', None)
    @patch('builtins.input', side_effect=['Nghia', 'Vo'])
    @patch('inCollege.ALL_STUDENT_ACCOUNTS', {"wyoming44":{"lastName":"Vo", "firstName":"Nghia"}})
    def testUserInTheSystemWhenNotLoggedIn(self, mock_input):
        expected_output = "They are a part of the InCollege system."
        out = io.StringIO()
        with redirect_stdout(out):
            find()
        self.assertEqual(out.getvalue().strip(), expected_output)

    #test user not in the system when not logged in
    @patch('inCollege.globalUsername', None)
    @patch('builtins.input', side_effect=['Nghia', 'Vo'])
    @patch('inCollege.ALL_STUDENT_ACCOUNTS', {"wyoming44":{"lastName":"Vo", "firstName":"Jason"}})
    def testUserNotInTheSystemWhenNotLoggedIn(self, mock_input):
        expected_output = "They are not a part of the InCollege system yet."
        out = io.StringIO()
        with redirect_stdout(out):
            find()
        self.assertEqual(out.getvalue().strip(), expected_output)

    #test user logged in and search by last name but not found
    @patch('inCollege.globalUsername', 'epic4coming')
    @patch('builtins.input', side_effect=['1', 'Wong'])
    @patch('inCollege.ALL_STUDENT_ACCOUNTS', {"wyoming44":{"lastName":"Vo", "firstName":"Jason"}})
    def testUserLoggedInAndSearchByLastName_notFound(self, mock_input):
        expected_output = "No one was found with that last name"
        out = io.StringIO()
        with redirect_stdout(out):
            find()
        value = expected_output in out.getvalue().strip()
        assert value == True

    #test user logged in and search by last name and found, but wrong digit number when look up
    @patch('inCollege.globalUsername', 'epic4coming')
    @patch('builtins.input', side_effect=['1', 'Vo', '-1'])
    @patch('inCollege.ALL_STUDENT_ACCOUNTS', {"wyoming44":{'university':"SJSU","lastName":"Vo", "firstName":"Jason", "major":"CS"}})
    def testUserLoggedInAndSearchByLastName_found_wrongDigitNumber(self, mock_input):
        expected_output = "0. Jason Vo, SJSU, CS"
        out = io.StringIO()
        with redirect_stdout(out):
            find()
        value = expected_output in out.getvalue().strip()
        assert value == True

    #test user logged in and search by last name and found, but accurate digit number when look up
    @patch('inCollege.globalUsername', 'wyoming55')
    @patch('builtins.input', side_effect=['1', 'Vo','0'])
    def testUserLoggedInAndSearchByLastName_found_rightDigitNumber(self, mock_input):
        out = io.StringIO()
        with mock.patch('inCollege.ALL_STUDENT_ACCOUNTS',  {"wyoming44":{'university':"SJSU","lastName":"Vo", "firstName":"Jason", "major":"CS", 'requests': []}, "wyoming55":{'university':"SJSU","lastName":"Tran", "firstName":"Kevin", "major":"CS", 'requests': []}}) as mocked_find:
            find()
            assert mocked_find['wyoming44']['requests'] == ['wyoming55']


    #test user logged in and search by university and not found
    @patch('inCollege.globalUsername', 'wyoming55')
    @patch('builtins.input', side_effect=['2', 'USF'])
    @patch('inCollege.ALL_STUDENT_ACCOUNTS',  {"wyoming44":{'university':"SJSU","lastName":"Vo", "firstName":"Jason", "major":"CS", 'requests': []}, "wyoming55":{'university':"SJSU","lastName":"Tran", "firstName":"Kevin", "major":"CS", 'requests': []}})
    def testUserLoggedInAndSearchByUniversity_notFound(self, mock_input):
        expected_output = "No one was found in that university"
        out = io.StringIO()
        with redirect_stdout(out):
            find()
        self.assertTrue(expected_output in out.getvalue().strip())

    #test user logged in and search by university and found and enter wrong digit number
    @patch('inCollege.globalUsername', 'wyoming55')
    @patch('builtins.input', side_effect=['2', 'SJSU', "-1"])
    @patch('inCollege.ALL_STUDENT_ACCOUNTS',  {"wyoming44":{'university':"SJSU","lastName":"Vo", "firstName":"Jason", "major":"CS", 'requests': []}, "wyoming55":{'university':"USF","lastName":"Tran", "firstName":"Kevin", "major":"CS", 'requests': []}})
    def testUserLoggedInAndSearchByUniversity_Found_butWrongDigitNumber(self, mock_input):
        expected_output = "0. Jason Vo, SJSU, CS"
        out = io.StringIO()
        with redirect_stdout(out):
            find()
        self.assertTrue(expected_output in out.getvalue().strip())

    #test user logged in and search by university and found and enter right digit number
    @patch('inCollege.globalUsername', 'wyoming55')
    @patch('builtins.input', side_effect=['2', 'SJSU', "0"])
    @patch('inCollege.ALL_STUDENT_ACCOUNTS',  {"wyoming44":{'university':"SJSU","lastName":"Vo", "firstName":"Jason", "major":"CS", 'requests': []}, "wyoming55":{'university':"USF","lastName":"Tran", "firstName":"Kevin", "major":"CS", 'requests': []}})
    def testUserLoggedInAndSearchByUniversity_Found_butRightDigitNumber(self, mock_input):
        out = io.StringIO()
        with mock.patch('inCollege.ALL_STUDENT_ACCOUNTS',  {"wyoming44":{'university':"SJSU","lastName":"Vo", "firstName":"Jason", "major":"CS", 'requests': []}, "wyoming55":{'university':"USF","lastName":"Tran", "firstName":"Kevin", "major":"CS", 'requests': []}}) as mocked_find:
            find()
            assert mocked_find['wyoming44']['requests'] == ['wyoming55']

    #test user logged in and search by major and not found
    @patch('inCollege.globalUsername', 'wyoming55')
    @patch('builtins.input', side_effect=['3', 'Business Analytics'])
    @patch('inCollege.ALL_STUDENT_ACCOUNTS',  {"wyoming44":{'university':"SJSU","lastName":"Vo", "firstName":"Jason", "major":"CS", 'requests': []}, "wyoming55":{'university':"SJSU","lastName":"Tran", "firstName":"Kevin", "major":"CSE", 'requests': []}})
    def testUserLoggedInAndSearchByMajor_notFound(self, mock_input):
        expected_output = "No one was found with that major"
        out = io.StringIO()
        with redirect_stdout(out):
            find()
        self.assertTrue(expected_output in out.getvalue().strip())

    #test user logged in and search by major and found with wrong digit number
    @patch('inCollege.globalUsername', 'wyoming55')
    @patch('builtins.input', side_effect=['3', 'CS', '-1'])
    @patch('inCollege.ALL_STUDENT_ACCOUNTS',  {"wyoming44":{'university':"SJSU","lastName":"Vo", "firstName":"Jason", "major":"CS", 'requests': []}, "wyoming55":{'university':"SJSU","lastName":"Tran", "firstName":"Kevin", "major":"CS", 'requests': []}})
    def testUserLoggedInAndSearchByMajor_notFound_wrongDigit(self, mock_input):
        expected_output = "0. Jason Vo, SJSU, CS"
        out = io.StringIO()
        with redirect_stdout(out):
            find()
        self.assertTrue(expected_output in out.getvalue().strip())


    #test user logged in and search by major and found with right digit number
    @patch('inCollege.globalUsername', 'wyoming55')
    @patch('builtins.input', side_effect=['3', 'CS', '0'])
    @patch('inCollege.ALL_STUDENT_ACCOUNTS',  {"wyoming44":{'university':"SJSU","lastName":"Vo", "firstName":"Jason", "major":"CS", 'requests': []}, "wyoming55":{'university':"SJSU","lastName":"Tran", "firstName":"Kevin", "major":"CS", 'requests': []}})
    def testUserLoggedInAndSearchByMajor_Found_RightDigit(self, mock_input):
        out = io.StringIO()
        with mock.patch('inCollege.ALL_STUDENT_ACCOUNTS',  {"wyoming44":{'university':"SJSU","lastName":"Vo", "firstName":"Jason", "major":"CS", 'requests': []}, "wyoming55":{'university':"SJSU","lastName":"Tran", "firstName":"Kevin", "major":"CS", 'requests': []}}) as mocked_find:
            find()
            assert mocked_find['wyoming44']['requests'] == ['wyoming55']


    #test if the profile major can be changed
    @patch('inCollege.globalUsername', 'wyoming55')
    @patch('builtins.input', side_effect=['2', 'CS', '8'])
    @patch('inCollege.ALL_STUDENT_ACCOUNTS',  {"wyoming44":{'university':"SJSU","lastName":"Vo", "firstName":"Jason", "major":"CS", 'requests': []}, "wyoming55":{'university':"SJSU","lastName":"Tran", "firstName":"Kevin", "major":"CS", 'requests': []}})
    @patch('inCollege.ALL_PROFILES',  {"wyoming44":{'university':"SJSU","lastName":"Vo", "firstName":"Jason", "major":"CS", 'requests': []}, "wyoming55":{'university':"SJSU","lastName":"Tran", "firstName":"Kevin", "major":"Nursing", 'requests': []}})
    def test_change_major(self, mock_input):
        out = StringIO()
        with patch('sys.stdout', out):
            profileChange()

        expected_output = "You successfuly changed your major!"
        self.assertIn(expected_output, out.getvalue())

    #test if the profile university can be changed
    @patch('inCollege.globalUsername', 'wyoming55')
    @patch('builtins.input', side_effect=['3', 'New University', '8'])
    @patch('inCollege.ALL_STUDENT_ACCOUNTS',  {"wyoming44":{'university':"SJSU","lastName":"Vo", "firstName":"Jason", "major":"CS", 'requests': []}, "wyoming55":{'university':"SJSU","lastName":"Tran", "firstName":"Kevin", "major":"CS", 'requests': []}})
    @patch('inCollege.ALL_PROFILES',  {"wyoming44":{'university':"SJSU","lastName":"Vo", "firstName":"Jason", "major":"CS", 'requests': []}, "wyoming55":{'university':"SJSU","lastName":"Tran", "firstName":"Kevin", "major":"Nursing", 'requests': []}})
    def test_change_university(self, mock_input):
        out = StringIO()
        with patch('sys.stdout', out):
            profileChange()

        expected_output = "You successfuly changed your university!"
        self.assertIn(expected_output, out.getvalue())

    #test if the profile "new about section" can be changed
    @patch('inCollege.globalUsername', 'wyoming55')
    @patch('builtins.input', side_effect=['4', 'New About Section', '8'])
    @patch('inCollege.ALL_STUDENT_ACCOUNTS',  {"wyoming44":{'university':"SJSU","lastName":"Vo", "firstName":"Jason", "major":"CS", 'requests': []}, "wyoming55":{'university':"SJSU","lastName":"Tran", "firstName":"Kevin", "major":"CS", 'requests': []}})
    @patch('inCollege.ALL_PROFILES',  {"wyoming44":{'university':"SJSU","lastName":"Vo", "firstName":"Jason", "major":"CS", 'requests': []}, "wyoming55":{'university':"SJSU","lastName":"Tran", "firstName":"Kevin", "major":"Nursing", 'requests': []}})
    def test_change_about_section(self, mock_input):
        out = StringIO()
        with patch('sys.stdout', out):
            profileChange()

        expected_output = "You successfuly changed your about section!"
        self.assertIn(expected_output, out.getvalue())



    #Test to view friends profile 
    @patch('inCollege.globalUsername', 'wyoming55')
    @patch('builtins.input', side_effect=['1'])
    @patch('inCollege.ALL_STUDENT_ACCOUNTS', {
        "wyoming55": {'university': "SJSU", 'lastName': "YourLastName", 'firstName': "YourFirstName", 'major': "YourMajor", 'friends': ["wyoming56", "wyoming44", "wyoming45", "wyoming57"]},
        "wyoming44": {'university': "SJSU", 'lastName': "Vo", 'firstName': "Jason", 'major': "CS", 'requests': []},
        "wyoming56": {'university': "SJSU", 'lastName': "Smith", 'firstName': "Alice", 'major': "Engineering", 'requests': []},
        "wyoming45": {'university': "SJSU", 'lastName': "User", 'firstName': "Test", 'major': "CS", 'requests': []},
        "wyoming57": {'university': "SJSU", 'lastName': "Raven", 'firstName': "Faith", 'major': "Engineering", 'requests': []},
    })
    @patch('inCollege.ALL_PROFILES', {
        "wyoming55": {'title': "", 'about': "", 'education': "", 'university': "SJSU", 'lastName': "YourLastName", 'firstName': "YourFirstName", 'major': "YourMajor", 'friends': ["wyoming56", "wyoming44", "wyoming45", "wyoming57"], 'job_title': ["Test Job"], 'job_employer': ["Test Employer"], 'job_date_start': ["Test Date Start"], 'job_date_end': ["Test Date End"], 'job_location': ["Test Location"], 'job_description': ["Test Description"]},
        "wyoming44": {'title': "", 'about': "", 'education': "", 'university': "SJSU", 'lastName': "Vo", 'firstName': "Jason", 'major': "CS", 'requests': [], 'job_title': ["Test Job"], 'job_employer': ["Test Employer"], 'job_date_start': ["Test Date Start"], 'job_date_end': ["Test Date End"], 'job_location': ["Test Location"], 'job_description': ["Test Description"]},
        "wyoming56": {'title': "", 'about': "", 'education': "", 'university': "SJSU", 'lastName': "Smith", 'firstName': "Alice", 'major': "Engineering", 'requests': [], 'job_title': ["Test Job"], 'job_employer': ["Test Employer"], 'job_date_start': ["Test Date Start"], 'job_date_end': ["Test Date End"], 'job_location': ["Test Location"], 'job_description': ["Test Description"]},
        "wyoming45": {'title': "", 'about': "", 'education': "", 'university': "SJSU", 'lastName': "User", 'firstName': "Test", 'major': "CS", 'requests': [], 'job_title': ["Test Job"], 'job_employer': ["Test Employer"], 'job_date_start': ["Test Date Start"], 'job_date_end': ["Test Date End"], 'job_location': ["Test Location"], 'job_description': ["Test Description"]},
        "wyoming57": {'title': "", 'about': "", 'education': "", 'university': "SJSU", 'lastName': "Raven", 'firstName': "Faith", 'major': "Engineering", 'requests': [], 'job_title': ["Test Job"], 'job_employer': ["Test Employer"], 'job_date_start': ["Test Date Start"], 'job_date_end': ["Test Date End"], 'job_location': ["Test Location"], 'job_description': ["Test Description"]},
    })
    def test_view_friend_profile(self, mock_input):
        # Redirect the function's output to capture it
        out = StringIO()
        with patch('sys.stdout', out):
            viewFriendsProfiles()

        # Verify that the friend's profile is correctly displayed
        expected_output = "Alice Smith's Profile:\n"
        self.assertIn(expected_output, out.getvalue())
        self.assertIn("Title: ", out.getvalue())
        self.assertIn("Major: Engineering", out.getvalue())
        self.assertIn("University: SJSU", out.getvalue())
        self.assertIn("About: ", out.getvalue())
        self.assertIn("Education: ", out.getvalue())


    @patch('inCollege.globalUsername', 'wyoming55')
    @patch('inCollege.ALL_STUDENT_ACCOUNTS', {
        "wyoming55": {'university': "SJSU", 'lastName': "YourLastName", 'firstName': "YourFirstName", 'major': "YourMajor", 'friends': []},  # Add the 'friends' key here
        "wyoming44": {'university': "SJSU", 'lastName': "Vo", 'firstName': "Jason", 'major': "CS", 'requests': []},
    })
    def test_view_non_friend_profile(self):
    # Redirect the function's output to capture it
        out = StringIO()
        with patch('sys.stdout', out):
            viewFriendsProfiles()

    # Verify that the function correctly handles non-friends
        expected_output = "You have not added any friends yet"
        self.assertIn(expected_output, out.getvalue())


    #Test Case to display list of friends
    @patch('inCollege.globalUsername', 'wyoming55')
    @patch('builtins.input', side_effect=['2', 'exit', '3'])
    @patch('inCollege.ALL_STUDENT_ACCOUNTS', {
        "wyoming55": {'university': "SJSU", 'lastName': "YourLastName", 'firstName': "YourFirstName", 'major': "YourMajor", 'friends': ["wyoming44", "wyoming56"]},
        "wyoming44": {'university': "SJSU", 'lastName': "Vo", 'firstName': "Jason", 'major': "CS", 'requests': []},
        "wyoming56": {'university': "SJSU", 'lastName': "Smith", 'firstName': "Alice", 'major': "Engineering", 'requests': []},
    })
    @patch('inCollege.ALL_PROFILES', {
        "wyoming55": {'title': "", 'about': "", 'education': "", 'university': "SJSU", 'lastName': "YourLastName", 'firstName': "YourFirstName", 'major': "YourMajor", 'friends': ["wyoming56", "wyoming44", "wyoming45", "wyoming57"], 'job_title': ["Test Job"], 'job_employer': ["Test Employer"]},
        "wyoming44": {'title': "", 'about': "", 'education': "", 'university': "SJSU", 'lastName': "Vo", 'firstName': "Jason", 'major': "CS"},
        "wyoming56": {'title': "", 'about': "", 'education': "", 'university': "SJSU", 'lastName': "Smith", 'firstName': "Alice", 'major': "Engineering", 'requests': []},
        "wyoming45": {'title': "", 'about': "", 'education': "", 'university': "SJSU", 'lastName': "User", 'firstName': "Test", 'major': "CS", 'requests': []},
        "wyoming57": {'title': "", 'about': "", 'education': "", 'university': "SJSU", 'lastName': "Raven", 'firstName': "Faith", 'major': "Engineering", 'requests': []},
    })
    def test_display_friends_list(self, mock_input):
        # Redirect the function's output to capture it
        out = StringIO()
        with patch('sys.stdout', out):
            showMyNetwork()

        # Verify that the list of friends is displayed
        # Note: The test below works now but if it's supposed to say
        # 1. Jason Vo, SJSU, CS
        # 2. Alice Smith, SJSU, Engineering
        # then the code is starting from 0 rather than 1
        expected_output = "0. Jason Vo, SJSU, CS"
        self.assertIn(expected_output, out.getvalue())
        expected_output = "1. Alice Smith, SJSU, Engineering"
        self.assertIn(expected_output, out.getvalue())


class TestInCollegeFeatures(unittest.TestCase):


    @patch('inCollege.globalUsername', 'test_user')
    @patch('builtins.input', side_effect=["Test Job 10", "It's test job 10", "employer10", "Tampa", "80000"])
    @patch('inCollege.ALL_STUDENT_ACCOUNTS', {
        "test_user": {'firstName': "Test", 'lastName': "User"},
    })
    @patch('inCollege.ALL_JOBS', {
        "Test Job 1": {'description': "It's test job 1", 'employer': "employer1", 'location': "Tampa", 'salary': "80000", 'poster': "other_user", 'applicants': set(), 'applications': set(), 'saved': False},
        "Test Job 2": {'description': "It's test job 2", 'employer': "employer2", 'location': "Tampa", 'salary': "80000", 'poster': "other_user", 'applicants': set(), 'applications': set(), 'saved': False},
        "Test Job 3": {'description': "It's test job 3", 'employer': "employer3", 'location': "Tampa", 'salary': "80000", 'poster': "other_user", 'applicants': set(), 'applications': set(), 'saved': False},
        "Test Job 4": {'description': "It's test job 4", 'employer': "employer4", 'location': "Tampa", 'salary': "80000", 'poster': "other_user", 'applicants': set(), 'applications': set(), 'saved': False},
        "Test Job 5": {'description': "It's test job 5", 'employer': "employer5", 'location': "Tampa", 'salary': "80000", 'poster': "other_user", 'applicants': set(), 'applications': set(), 'saved': False},
        "Test Job 6": {'description': "It's test job 6", 'employer': "employer6", 'location': "Tampa", 'salary': "80000", 'poster': "other_user", 'applicants': set(), 'applications': set(), 'saved': False},
        "Test Job 7": {'description': "It's test job 7", 'employer': "employer7", 'location': "Tampa", 'salary': "80000", 'poster': "other_user", 'applicants': set(), 'applications': set(), 'saved': False},
        "Test Job 8": {'description': "It's test job 8", 'employer': "employer8", 'location': "Tampa", 'salary': "80000", 'poster': "other_user", 'applicants': set(), 'applications': set(), 'saved': False},
        "Test Job 9": {'description': "It's test job 9", 'employer': "employer9", 'location': "Tampa", 'salary': "80000", 'poster': "other_user", 'applicants': set(), 'applications': set(), 'saved': False},
    })
    def test_post_jobs(self, mock_input):
        out = StringIO()
        with patch('sys.stdout', out):
            inCollege.postJob()
        
        expected_output = "You have successfully posted a job!"
        self.assertIn(expected_output, out.getvalue())
    

    @patch('inCollege.globalUsername', 'test_user')
    @patch('builtins.input', side_effect=["Test Job 11", "It's test job 11", "employer11", "Tampa", "80000"])
    @patch('inCollege.ALL_STUDENT_ACCOUNTS', {
        "test_user": {'firstName': "Test", 'lastName': "User"},
    })
    @patch('inCollege.ALL_JOBS', {
        "Test Job 1": {'description': "It's test job 1", 'employer': "employer1", 'location': "Tampa", 'salary': "80000", 'poster': "other_user", 'applicants': set(), 'applications': set(), 'saved': False},
        "Test Job 2": {'description': "It's test job 2", 'employer': "employer2", 'location': "Tampa", 'salary': "80000", 'poster': "other_user", 'applicants': set(), 'applications': set(), 'saved': False},
        "Test Job 3": {'description': "It's test job 3", 'employer': "employer3", 'location': "Tampa", 'salary': "80000", 'poster': "other_user", 'applicants': set(), 'applications': set(), 'saved': False},
        "Test Job 4": {'description': "It's test job 4", 'employer': "employer4", 'location': "Tampa", 'salary': "80000", 'poster': "other_user", 'applicants': set(), 'applications': set(), 'saved': False},
        "Test Job 5": {'description': "It's test job 5", 'employer': "employer5", 'location': "Tampa", 'salary': "80000", 'poster': "other_user", 'applicants': set(), 'applications': set(), 'saved': False},
        "Test Job 6": {'description': "It's test job 6", 'employer': "employer6", 'location': "Tampa", 'salary': "80000", 'poster': "other_user", 'applicants': set(), 'applications': set(), 'saved': False},
        "Test Job 7": {'description': "It's test job 7", 'employer': "employer7", 'location': "Tampa", 'salary': "80000", 'poster': "other_user", 'applicants': set(), 'applications': set(), 'saved': False},
        "Test Job 8": {'description': "It's test job 8", 'employer': "employer8", 'location': "Tampa", 'salary': "80000", 'poster': "other_user", 'applicants': set(), 'applications': set(), 'saved': False},
        "Test Job 9": {'description': "It's test job 9", 'employer': "employer9", 'location': "Tampa", 'salary': "80000", 'poster': "other_user", 'applicants': set(), 'applications': set(), 'saved': False},
        "Test Job 10": {'description': "It's test job 10", 'employer': "employer10", 'location': "Tampa", 'salary': "80000", 'poster': "other_user", 'applicants': set(), 'applications': set(), 'saved': False},
    })
    def test_no_more_than_10_jobs(self, mock_input):
        out = StringIO()
        with patch('sys.stdout', out):
            inCollege.postJob()
        
        expected_output = "Sorry, all permitted jobs have been created. Please come back later.\n"
        self.assertIn(expected_output, out.getvalue())


    @patch('inCollege.globalUsername', 'job_poster')
    @patch('builtins.input', side_effect=["Test Job 1"])
    @patch('inCollege.ALL_JOBS', {
        "Test Job 1": {'applicants': {'test_user', 'another_user'}, 'saved': False, 'poster': 'job_poster'},
        "Test Job 2": {'applicants': {'test_user', 'another_user'}, 'saved': False, 'poster': 'job_poster'},
    })
    def test_delete_job_and_applications(self, mock_input):
        out = StringIO()
        with patch('sys.stdout', out):
            inCollege.deleteJob("job_poster")
        
        expected_output = "Job deleted"
        self.assertIn(expected_output, out.getvalue())

    
    @patch('inCollege.globalUsername', 'test_user')
    @patch('builtins.input', side_effect=["Test Job", "2024", "Immediately", "I am a good fit"])
    @patch('inCollege.ALL_JOBS', {
        "Test Job": {'poster': "other_user", 'applicants': set(), 'applications': set()}
    })
    def test_apply_job(self, mock_input):
        out = StringIO()
        with patch('sys.stdout', out):
            inCollege.applyJob()
        
        expected_output = "You have successfully applied to the job"
        self.assertIn(expected_output, out.getvalue())

    
    @patch('inCollege.globalUsername', 'test_user')
    @patch('builtins.input', side_effect=["Test Job"])
    @patch('inCollege.ALL_JOBS', {
        "Test Job": {'saved': False}
    })
    def test_save_job(self, mock_input):
        out = StringIO()
        with patch('sys.stdout', out):
            inCollege.saveJob()
        
        expected_output = "You have successfully saved the job"
        self.assertIn(expected_output, out.getvalue())


    @patch('inCollege.globalUsername', 'test_user')
    @patch('builtins.input', side_effect=["Test Job"])
    @patch('inCollege.ALL_JOBS', {
        "Test Job": {'saved': True}
    })
    def test_unsave_job(self, mock_input):
        out = StringIO()
        with patch('sys.stdout', out):
            inCollege.saveJob()
        
        expected_output = "You have successfully saved the job"
        self.assertNotIn(expected_output, out.getvalue())


    @patch('builtins.input')
    def test_cannot_apply_for_own_job(self, mock_input):
        inCollege.globalUsername = 'test_user'
        inCollege.ALL_JOBS['My Own Job'] = {'applicants': set(), 'saved': False, 'poster': 'test_user'}

        prompts_apply = ["My Own Job", "2024", "Immediately", "I am a good fit"]
        mock_input.side_effect = prompts_apply

        inCollege.applyJob()
        self.assertNotIn('test_user', inCollege.ALL_JOBS['My Own Job']['applicants'])


    @patch('inCollege.globalUsername', 'test_user')
    @patch('builtins.input', side_effect=["Test Job", "2024", "Immediately", "I am a good fit", "Test Job"])
    @patch('inCollege.ALL_JOBS', {
        "Test Job": {'poster': "other_user", 'applicants': set(), 'applications': set()}
    })
    def test_cannot_apply_twice(self, mock_input):
        out = StringIO()
        inCollege.applyJob()
        with patch('sys.stdout', out):
            inCollege.applyJob()
        
        expected_output = "You have already applied to this job"
        self.assertIn(expected_output, out.getvalue())


    @patch('builtins.input')
    def test_student_notified_on_deleted_job(self, mock_input):
        inCollege.globalUsername = 'job_poster'
        inCollege.ALL_JOBS['Job To Notify'] = {'applicants': {'test_user'}, 'saved': False, 'poster': 'job_poster'}
        inCollege.deleteJobNotification = {}  # Reset notifications

        inCollege.deleteJob('job_poster')
        self.assertIn('test_user', inCollege.deleteJobNotification)
        self.assertIn('Job To Notify', inCollege.deleteJobNotification['test_user'])


    @patch('inCollege.globalUsername', 'test_user')
    @patch('builtins.input', side_effect=["Test Job 1", "3"])
    @patch('inCollege.ALL_JOBS', {
        "Test Job 1": {'applicants': {'test_user', 'another_user'}, 'saved': False, 'poster': 'job_poster'},
        "Test Job 2": {'applicants': {'test_user', 'another_user'}, 'saved': False, 'poster': 'job_poster'},
    })
    def test_student_notified_on_deleted_job(self, mock_input):
        out = StringIO()
        inCollege.deleteJob("job_poster")
        with patch('sys.stdout', out):
            inCollege.jobSearch()
        
        expected_output = "A job you have applied to has been deleted"
        self.assertIn(expected_output, out.getvalue())

    
    @patch('inCollege.globalUsername', 'test_user')
    @patch('builtins.input', side_effect=["Test Job"])
    @patch('inCollege.ALL_JOBS', {
        "Test Job": {'saved': "Test Job"}
    })
    def test_unsave_job(self, mock_input):
        out = StringIO()
        with patch('sys.stdout', out):
            inCollege.saveJob()
        
        expected_output = "You have successfully saved the job"
        self.assertNotIn(expected_output, out.getvalue())

    
    @patch('inCollege.globalUsername', 'test_user')
    @patch('builtins.input', side_effect=["7"])
    @patch('inCollege.ALL_JOBS', {
        "Test Job": {'saved': "Test Job"}
    })
    def test_view_job(self, mock_input):
        out = StringIO()
        with patch('sys.stdout', out):
            inCollege.saveJob()
        
        expected_output = "You have successfully saved the job"
        self.assertNotIn(expected_output, out.getvalue())


if __name__ == '__main__':
    unittest.main()
