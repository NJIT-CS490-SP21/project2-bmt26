import unittest
import os
import sys

sys.path.append(os.path.abspath('../../'))
from app import log_chat
import user_template

KEY_INPUT = "input"
KEY_USERNAME = "user"
KEY_EXPECTED = "expected"

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
                KEY_EXPECTED: '<user>: Test-/+*0\'Sentence',
            },
            {
                KEY_INPUT: '',
                KEY_USERNAME: "sfes_asdf",
                KEY_EXPECTED: '<user>: ',
            },
            {
                KEY_INPUT: '\n\n\n',
                KEY_USERNAME: "tictac",
                KEY_EXPECTED: '<user>: \n\n\n',
            },
        ]
        
    def test_username_success(self):
        for test in self.success_test_params:
            data = {'username': KEY_USERNAME, 'message': test[KEY_INPUT]}
            actual_result = log_chat(data)
            
            expected_result = test[KEY_EXPECTED]
            
            self.assertEqual(len(actual_result), len(expected_result))
            self.assertEqual(actual_result, expected_result)

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
                KEY_EXPECTED: '<user>: Test-/+*0\'Sentence',
            },
            {
                KEY_INPUT: '',
                KEY_USERNAME: "sfes_asdf",
                KEY_EXPECTED: '<user>: ',
            },
            {
                KEY_INPUT: '\n\n\n',
                KEY_USERNAME: "tictac",
                KEY_EXPECTED: '<user>: \n\n\n',
            },
        ]
        
    def test_username_success(self):
        for test in self.success_test_params:
            data = {'username': KEY_USERNAME, 'message': test[KEY_INPUT]}
            actual_result = log_chat(data)
            
            expected_result = test[KEY_EXPECTED]
            
            self.assertEqual(len(actual_result), len(expected_result))
            self.assertEqual(actual_result, expected_result)

if __name__ == '__main__':
    unittest.main()