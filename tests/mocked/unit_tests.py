"""Tests app.py for mocked functions"""
import unittest
import unittest.mock as mock
from unittest.mock import patch
import os
import sys

sys.path.append(os.path.abspath('../../'))
from app import login, update_score
import user_template

KEY_INPUT = "input"
KEY_USERNAME = "user"
KEY_EXPECTED = "expected"
KEY_LETTER = "letter"

INITIAL_USERNAME = 'James'
INITIAL_RANK = 100
INITIAL_USERLIST = ['user', 'james', 'sfes_asdf', 'tictac']

class LoginTestCase(unittest.TestCase):
    """Test Case For Logging In"""
    def setUp(self):
        """Variable and Expected Outcome Declartion"""
        self.success_test_params = [
            {
                KEY_USERNAME: 'user',
                KEY_EXPECTED: [INITIAL_USERNAME, 'user'],
            },
            {
                KEY_USERNAME: '-/+*0\'',
                KEY_EXPECTED: [INITIAL_USERNAME, 'user', '-/+*0\''],
            },
            {
                KEY_USERNAME: ' ',
                KEY_EXPECTED: [INITIAL_USERNAME, 'user', '-/+*0\'', ' '],
            },
        ]

        initial_user = user_template.Template(username=INITIAL_USERNAME, rank=100)
        self.initial_db_mock = [initial_user]


    def mocked_db_session_add(self, username):
        """Mock of db add"""
        self.initial_db_mock.append(username)

    def mocked_db_session_commit(self):
        """Mock of db commit"""
        pass

    def mocked_template_query_all(self):
        """Mock of db query"""
        return self.initial_db_mock

    def test_login_success(self):
        """Implementation of Login Test"""
        for test in self.success_test_params:
            with patch('app.DB.session.add', self.mocked_db_session_add):
                with patch('app.DB.session.commit', self.mocked_db_session_commit):
                    with patch('user_template.Template.query') as mocked_query:
                        mocked_query.all = self.mocked_template_query_all

                        actual_result = login({'username': test[KEY_USERNAME]})
                        expected_result = test[KEY_EXPECTED]

                        self.assertEqual(len(actual_result), len(expected_result))
                        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
