import unittest
import io
from inCollege import *
from contextlib import redirect_stdout
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

if __name__ == '__main__':
    unittest.main()