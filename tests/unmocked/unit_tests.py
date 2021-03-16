import unittest
import os
import sys

sys.path.append(os.path.abspath('../../'))
from app import add_user, log_chat, remove_user
import user_template

KEY_INPUT = "input"
KEY_USERNAME = "user"
KEY_EXPECTED = "expected"

INITIAL_USERLIST = ['user', 'james', 'sfes_asdf', 'tictac']

class SendChatTestCase(unittest.TestCase):
    def setUp(self):
        self.success_test_params = [
            {
                KEY_INPUT: 'Test Sentence',
                KEY_USERNAME: "user",
                KEY_EXPECTED: '<user>: Test Sentence',
            },
            {
                KEY_INPUT: 'Test-/+*0\'Sentence',
                KEY_USERNAME: "james",
                KEY_EXPECTED: '<james>: Test-/+*0\'Sentence',
            },
            {
                KEY_INPUT: '',
                KEY_USERNAME: "sfes_asdf",
                KEY_EXPECTED: '<sfes_asdf>: ',
            },
            {
                KEY_INPUT: '\n\n\n',
                KEY_USERNAME: "tictac",
                KEY_EXPECTED: '<tictac>: \n\n\n',
            },
        ]
        
    def test_chat_success(self):
        for test in self.success_test_params:
            actual_result = log_chat({'username': test[KEY_USERNAME], 'message': test[KEY_INPUT]})
            
            expected_result = test[KEY_EXPECTED]
            
            self.assertEqual(len(actual_result), len(expected_result))
            self.assertEqual(actual_result, expected_result)

class RemoveAnyOneUserTestCase(unittest.TestCase):
    def setUp(self):
        self.success_test_params = [
            {
                KEY_USERNAME: "user",
                KEY_EXPECTED: ['james', 'sfes_asdf', 'tictac'],
            },
            {
                KEY_USERNAME: "james",
                KEY_EXPECTED: ['user', 'sfes_asdf', 'tictac'],
            },
            {
                KEY_USERNAME: "sfes_asdf",
                KEY_EXPECTED: ['user', 'james', 'tictac'],
            },
            {
                KEY_USERNAME: "tictac",
                KEY_EXPECTED: ['user', 'james', 'sfes_asdf'],
            },
        ]
        
    def test_remove_success(self):
        for person in INITIAL_USERLIST:
            add_user(person)
        for test in self.success_test_params:
            actual_result = remove_user(test[KEY_USERNAME])
            
            expected_result = test[KEY_EXPECTED]
            
            self.assertEqual(len(actual_result), len(expected_result))
            self.assertEqual(actual_result, expected_result)

if __name__ == '__main__':
    unittest.main()