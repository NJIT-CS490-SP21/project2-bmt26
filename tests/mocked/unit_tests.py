"""Tests app.py for mocked functions"""
import unittest
import unittest.mock as mock
from unittest.mock import patch
import os
import sys

sys.path.append(os.path.abspath('../../'))
from app import login, update_score, add_user
import user_template

KEY_INPUT = "input"
KEY_USERNAME = "user"
KEY_EXPECTED = "expected"
KEY_FACE = "face"

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

        initial_user = user_template.Template(username=INITIAL_USERNAME,
                                              rank=100)
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
                with patch('app.DB.session.commit',
                           self.mocked_db_session_commit):
                    with patch('user_template.Template.query') as mocked_query:
                        mocked_query.all = self.mocked_template_query_all

                        actual_result = login({'username': test[KEY_USERNAME]})
                        expected_result = test[KEY_EXPECTED]

                        self.assertEqual(len(actual_result),
                                         len(expected_result))
                        self.assertEqual(actual_result, expected_result)

    #DB.session.add(newplayer)
    #DB.session.commit()
    #allusers = user_template.Template.query.all()


class UpdateUserTestCase(unittest.TestCase):
    def setUp(self):
        self.success_test_params = [
            {
                KEY_USERNAME: 'user',
                KEY_FACE: 'X',
                KEY_EXPECTED: '101 to 99',
            },
            {
                KEY_USERNAME: 'sfes_asdf',
                KEY_FACE: 'X',
                KEY_EXPECTED: '99 to 101',
            },
            {
                KEY_USERNAME: 'james',
                KEY_FACE: 'O',
                KEY_EXPECTED: '100 to 99',
            },
        ]

        initial_user1 = user_template.Template(username=INITIAL_USERLIST[0],
                                               rank=100)
        initial_user2 = user_template.Template(username=INITIAL_USERLIST[1],
                                               rank=100)
        initial_user3 = user_template.Template(username=INITIAL_USERLIST[2],
                                               rank=100)
        initial_user4 = user_template.Template(username=INITIAL_USERLIST[3],
                                               rank=100)
        self.initial_db_mock = [
            initial_user1,
            initial_user2,
            initial_user3,
            initial_user4,
        ]

        #winner = DB.session.query(user_template.Template).filter_by(username=temp['username']).first()
    def mocked_db_session_add(self, username):
        self.initial_db_mock.append(username)

    def mocked_db_session_commit(self):
        pass

    def mocked_template_query_all(self, i):
        for x in range(len(self.initial_db_mock)):
            if self.initial_db_mock[x].username == i:
                self.initial_db_mock[x].rank += 1
                self.initial_db_mock[x + 1].rank -= 1
                return self.initial_db_mock[x]
        return 0

    def test_update_user_success(self):
        for person in INITIAL_USERLIST:
            add_user(person)
        for test in self.success_test_params:
            with patch('app.DB.session.add', self.mocked_db_session_add):
                with patch('app.DB.session.commit',
                           self.mocked_db_session_commit):
                    with patch('app.DB.session.query') as mocked_query:
                        mocked_query.filter_by = self.mocked_template_query_all(
                            test[KEY_USERNAME])
                        update_score({
                            'face': test[KEY_FACE],
                            'username': test[KEY_USERNAME]
                        })
                        actual_result = str(
                            self.initial_db_mock[
                                self.success_test_params.index(test)].rank
                        ) + " to " + str(self.initial_db_mock[
                            self.success_test_params.index(test) + 1].rank)
                        expected_result = test[KEY_EXPECTED]

                        self.assertEqual(len(actual_result),
                                         len(expected_result))
                        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
