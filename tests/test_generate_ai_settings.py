# Import the necessary modules
import unittest
from generate_ai_settings import generate_ai_settings
from snapshot import Snapshot


class TestGenerateAISettings(unittest.TestCase):
    def test_generate_ai_settings(self):
        # Define the input parameters
        issue_body = '''# Issue Title

## Description

This is a description of the issue.

## AI Goals

- Goal 1
- Goal 2
- Goal 3
'''
        openai_key = '1234567890abcdef'
        issue_number = 123
        expected_output = '''ai_name: github-gpt
ai_role: software developer who is willing to review the issue described and commit appropriate fixes on a feature branch
ai_goals:
- Goal 1
- Goal 2
- Goal 3
'''
        # Call the function
        actual_output = generate_ai_settings(issue_body, openai_key, issue_number)
        # Compare the output to the expected output
        self.assertEqual(actual_output, expected_output)

    def test_generate_ai_settings_no_goals(self):
        # Define the input parameters
        issue_body = '''# Issue Title

## Description

This is a description of the issue.

'''
        openai_key = '1234567890abcdef'
        issue_number = 123
        expected_output = '''ai_name: github-gpt
ai_role: software developer who is willing to review the issue described and commit appropriate fixes on a feature branch
ai_goals:
- This is a description of the issue.
'''
        # Call the function
        actual_output = generate_ai_settings(issue_body, openai_key, issue_number)
        # Compare the output to the expected output
        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    # Define the snapshot directory
    snapshot_dir = 'snapshots'
    # Create the snapshot object
    snapshot = Snapshot(snapshot_dir)
    # Run the tests
    unittest.main(testRunner=snapshot)