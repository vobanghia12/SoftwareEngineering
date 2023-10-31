import unittest
from unittest.mock import patch
import inCollege

class TestInCollegeFeatures(unittest.TestCase):


    @patch('builtins.input')
    def test_post_jobs(self, mock_input):
        prompts = ["Title {}".format(i) for i in range(1, 12)]
        prompts.extend(["Description", "Employer", "Location", "Salary"] * 11)
        mock_input.side_effect = prompts

        # Test posting up to ten jobs
        for i in range(10):
            inCollege.postJob()
            self.assertEqual(len(inCollege.ALL_JOBS), i + 1)

        # Test trying to post an 11th job
        inCollege.postJob()
        self.assertEqual(len(inCollege.ALL_JOBS), 10)  # Length should still be 10

    @patch('builtins.input')
    def test_delete_job_and_applications(self, mock_input):
        inCollege.globalUsername = 'job_poster'
        inCollege.ALL_JOBS['Job To Delete'] = {'applicants': {'test_user', 'another_user'}, 'saved': False, 'poster': 'job_poster'}

        mock_input.side_effect = ["Job To Delete"]
        inCollege.deleteJob()

        # Ensure the job is deleted
        self.assertNotIn('Job To Delete', inCollege.ALL_JOBS)

        # Ensure the applications are removed
        for user in inCollege.ALL_STUDENT_ACCOUNTS:
            self.assertNotIn('Job To Delete', inCollege.ALL_STUDENT_ACCOUNTS[user].get('applied_jobs', set()))

    @patch('builtins.input')
    def test_apply_and_save_jobs(self, mock_input):
        inCollege.globalUsername = 'test_user'
        inCollege.ALL_STUDENT_ACCOUNTS['test_user'] = {}

        # Mock job to apply to and save
        inCollege.ALL_JOBS['Test Job'] = {'applicants': set(), 'saved': False, 'poster': 'other_user'}

        prompts_apply = ["Test Job", "2024", "Immediately", "I am a good fit"]
        mock_input.side_effect = prompts_apply
        inCollege.applyJob()
        self.assertIn('test_user', inCollege.ALL_JOBS['Test Job']['applicants'])

        prompts_save = ["Test Job"]
        mock_input.side_effect = prompts_save
        inCollege.saveJob()
        self.assertIn('test_user', inCollege.ALL_JOBS['Test Job']['saved_by'])

    @patch('builtins.input')
    def test_unsave_job(self, mock_input):
        inCollege.globalUsername = 'test_user'
        inCollege.ALL_STUDENT_ACCOUNTS['test_user'] = {'saved_jobs': {'Test Job'}}
        inCollege.ALL_JOBS['Test Job'] = {'applicants': set(), 'saved_by': {'test_user'}, 'poster': 'other_user'}

        prompts_unsave = ["Test Job"]
        mock_input.side_effect = prompts_unsave

        inCollege.unsaveJob()
        self.assertNotIn('Test Job', inCollege.ALL_STUDENT_ACCOUNTS['test_user']['saved_jobs'])

    @patch('builtins.input')
    def test_cannot_apply_for_own_job(self, mock_input):
        inCollege.globalUsername = 'test_user'
        inCollege.ALL_JOBS['My Own Job'] = {'applicants': set(), 'saved': False, 'poster': 'test_user'}

        prompts_apply = ["My Own Job", "2024", "Immediately", "I am a good fit"]
        mock_input.side_effect = prompts_apply

        inCollege.applyJob()
        self.assertNotIn('test_user', inCollege.ALL_JOBS['My Own Job']['applicants'])

    @patch('builtins.input')
    def test_cannot_apply_twice(self, mock_input):
        inCollege.globalUsername = 'test_user'
        inCollege.ALL_JOBS['Another Job'] = {'applicants': set(), 'saved': False, 'poster': 'other_user'}

        prompts_apply = ["Another Job", "2024", "Immediately", "I am a good fit"]
        mock_input.side_effect = prompts_apply * 2  # Attempt to apply twice

        inCollege.applyJob()
        inCollege.applyJob()
        self.assertEqual(len(inCollege.ALL_JOBS['Another Job']['applicants']), 1)

    @patch('builtins.input')
    def test_student_notified_on_deleted_job(self, mock_input):
        inCollege.globalUsername = 'job_poster'
        inCollege.ALL_JOBS['Job To Notify'] = {'applicants': {'test_user'}, 'saved': False, 'poster': 'job_poster'}
        inCollege.deleteJobNotification = {}  # Reset notifications

        inCollege.deleteJob('Job To Notify')
        self.assertIn('test_user', inCollege.deleteJobNotification)
        self.assertIn('Job To Notify', inCollege.deleteJobNotification['test_user'])

if __name__ == '__main__':
    unittest.main()
