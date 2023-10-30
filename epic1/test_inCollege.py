import unittest
import io
from inCollege import *
from contextlib import redirect_stdout
from io import StringIO
import mock
from unittest.mock import patch

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
    def test_change_major(self, mock_input):
        out = StringIO()
        with patch('sys.stdout', out):
            profileChange()

        expected_output = "New Title"
        self.assertIn(expected_output, out.getvalue())

    #test if the profile university can be changed
    @patch('inCollege.globalUsername', 'wyoming55')
    @patch('builtins.input', side_effect=['3', 'New University', '8'])
    @patch('inCollege.ALL_STUDENT_ACCOUNTS',  {"wyoming44":{'university':"SJSU","lastName":"Vo", "firstName":"Jason", "major":"CS", 'requests': []}, "wyoming55":{'university':"SJSU","lastName":"Tran", "firstName":"Kevin", "major":"CS", 'requests': []}})
    def test_change_university(self, mock_input):
        out = StringIO()
        with patch('sys.stdout', out):
            profileChange()

        expected_output = "New University"
        self.assertIn(expected_output, out.getvalue())

    #test if the profile "new about section" can be changed
    @patch('inCollege.globalUsername', 'wyoming55')
    @patch('builtins.input', side_effect=['4', 'New About Section', '8'])
    @patch('inCollege.ALL_STUDENT_ACCOUNTS',  {"wyoming44":{'university':"SJSU","lastName":"Vo", "firstName":"Jason", "major":"CS", 'requests': []}, "wyoming55":{'university':"SJSU","lastName":"Tran", "firstName":"Kevin", "major":"CS", 'requests': []}})
    def test_change_about_section(self, mock_input):
        out = StringIO()
        with patch('sys.stdout', out):
            profileChange()

        expected_output = "New About Section"
        self.assertIn(expected_output, out.getvalue())



    #Test to view friends profile 
    @patch('inCollege.globalUsername', 'wyoming55')
    @patch('inCollege.ALL_STUDENT_ACCOUNTS', {
        "wyoming44": {'university': "SJSU", 'lastName': "Vo", 'firstName': "Jason", 'major': "CS", 'requests': []},
        "wyoming56": {'university': "SJSU", 'lastName': "Smith", 'firstName': "Alice", 'major': "Engineering", 'requests': []},
    })
    def test_view_friend_profile(self):
        # Simulate a friend relationship
        ALL_STUDENT_ACCOUNTS['wyoming55']['friends'] = ['wyoming44', 'wyoming56']

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

    #Test to view other non-friends profile
    @patch('inCollege.globalUsername', 'wyoming55')
    @patch('inCollege.ALL_STUDENT_ACCOUNTS', {
        "wyoming44": {'university': "SJSU", 'lastName': "Vo", 'firstName': "Jason", 'major': "CS", 'requests': []},
    })
    def test_view_non_friend_profile(self):
        # Simulate no friend relationship
        ALL_STUDENT_ACCOUNTS['wyoming55']['friends'] = []

        # Redirect the function's output to capture it
        out = StringIO()
        with patch('sys.stdout', out):
            viewFriendsProfiles()

        # Verify that the function correctly handles non-friends
        expected_output = "You have not added any friends yet"
        self.assertIn(expected_output, out.getvalue())

    #Test Case to display list of friends
    @patch('inCollege.globalUsername', 'wyoming55')
    @patch('inCollege.ALL_STUDENT_ACCOUNTS', {
        "wyoming44": {'university': "SJSU", 'lastName': "Vo", 'firstName': "Jason", 'major': "CS", 'requests': []},
        "wyoming56": {'university': "SJSU", 'lastName': "Smith", 'firstName': "Alice", 'major': "Engineering", 'requests': []},
    })
    def test_display_friends_list(self):
        # Simulate friend relationships
        ALL_STUDENT_ACCOUNTS['wyoming55']['friends'] = ['wyoming44', 'wyoming56']

        # Redirect the function's output to capture it
        out = StringIO()
        with patch('sys.stdout', out):
            showMyNetwork()

        # Verify that the list of friends is displayed
        expected_output = "1. Jason Vo, SJSU, CS"
        self.assertIn(expected_output, out.getvalue())
        expected_output = "2. Alice Smith, SJSU, Engineering"
        self.assertIn(expected_output, out.getvalue())



if __name__ == '__main__':
    unittest.main()
