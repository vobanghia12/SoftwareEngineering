import unittest
import io
from inCollege import *
from contextlib import redirect_stdout
import mock
from unittest.mock import patch

class TestInCollege(unittest.TestCase):
    #test createAccount() with valid username and password
    @patch('builtins.input', side_effect=['new_username', 'Nghiavo555@'])
    def test_createAccount_valid_username_and_password(self, mock_input):
        expected_output = "Account has been created!"
        out = io.StringIO()
        with redirect_stdout(out):
            createAccount()
        self.assertEqual(out.getvalue().strip(), expected_output)
        self.assertEqual(ALL_STUDENT_ACCOUNTS, {'new_username': 'Nghiavo555@'})

    #test createAccount() with invalid password
    @patch('builtins.input', side_effect=['new_username', 'Nghiavo'])
    def test_createAccount_invalid_password(self, mock_input):
        #when password is wrong, it would prompt createAccount() again
        with mock.patch('inCollege.createAccount') as mocked_createAccount:
            createAccount()
            mocked_createAccount.assert_called_once()

    #test createAccount() with invalid username
    @patch('builtins.input', side_effect=['wyoming', 'Nghiavo555@'])
    @patch('inCollege.ALL_STUDENT_ACCOUNTS', {"wyoming":"Wyoming0917@"})
    def test_createAccount_invalid_username(self, mock_input):
        #when password is wrong, it would prompt createAccount() again
        with mock.patch('inCollege.createAccount') as mocked_createAccount:
            createAccount()
            mocked_createAccount.assert_called_once()

    #test check user existence
    @patch('inCollege.ALL_STUDENT_ACCOUNTS', {"wyoming":"Wyoming0917@"})
    def test_checkUser_existence(self):
        self.assertEqual(checkUser("wyoming", "Wyoming0917@"), True)
        self.assertEqual(checkUser("wyo", "Wyoming0917@"), False)

    #test check unique username
    @patch('inCollege.ALL_STUDENT_ACCOUNTS', {"wyoming":"Wyoming0917@"})
    def test_checkUniqueUsername(self):
        self.assertEqual(checkUniqueUsername("wyoming"), True)
        self.assertEqual(checkUniqueUsername("monkeyDLuffy"), False)

    #test check valid password
    def test_checkValidPassword(self):
        password = "Nghiavo555@"
        self.assertEqual(checkValidPassword(password), True)

    #test check invalid password
    def test_checkInvalidPassword(self):
        password = "123"
        self.assertEqual(checkValidPassword(password), False)

    #test jobSearch() option
    @patch('builtins.input', side_effect=['1'])
    def test_jobSearch_called(self, mock_input):
        with mock.patch('inCollege.jobSearch') as mocked_jobSearch:
            jobSearch()
            mocked_jobSearch.assert_called_once()

    #test find() option
    @patch('builtins.input', side_effect=['2'])
    def test_findOption_called(self, mock_input):
        with mock.patch('inCollege.find') as mocked_find:
            find()
            mocked_find.assert_called_once()

    #test learningNewSkill() option
    @patch('builtins.input', side_effect=['3'])
    def test_learningNewSkillOption_called(self, mock_input):
        with mock.patch('inCollege.learningNewSkill') as mocked_learningNewSkill:
            learningNewSkill()
            mocked_learningNewSkill.assert_called_once()

    #test initialScreen() option
    @patch('builtins.input', side_effect=['4'])
    def test_initialScreenOption_called(self, mock_input):
        with mock.patch('inCollege.initialScreen') as mocked_initialScreen:
            initialScreen()
            mocked_initialScreen.assert_called_once()

    #test check non-existing option
    @patch('builtins.input', side_effect=['5'])
    def test_otherOptions_called(self, mock_input):
        with mock.patch('inCollege.loggedinScreen') as mocked_otherOptions:
            loggedinScreen()
            mocked_otherOptions.assert_called_once()

    #test login successful
    @patch('builtins.input', side_effect=['1', 'testuser', 'testpass'])
    def test_login_successful(self, mock_input):
        with mock.patch("inCollege.loggedinScreen") as loggedinScreen:
                with mock.patch('inCollege.checkUser', return_value=True):
                    loggedinScreen()
                    loggedinScreen.assert_called_once()


if __name__ == '__main__':
    unittest.main()