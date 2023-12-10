"""Implement unit tests for the AI Assistant service."""

import unittest
import assistant_pb2
from client import *
from sample_data import *

class TestAIAssistantService(unittest.TestCase):
    sample_data = SampleData()

    def test_get_pr_description(self):
        committed_changes = [
            assistant_pb2.Change(
                file_path="file1.txt",
                change_type="Modified",
                change_content="Content of change 1"
            ),
            assistant_pb2.Change(
                file_path="file2.txt",
                change_type="Added",
                change_content="Content of change 2"
            )
        ]
        repository_url="https://github.com/17-625-API-Design-F23/final-team-project-team-resolvers"
        source_branch="comp3"
        response = get_pr_description(repository_url, source_branch, committed_changes)
        # see if response.PR_description is in sample_data.PR_description_list
        self.assertIn(response.PR_description, self.sample_data.PR_description_list)

    def test_smart_auto_complete(self):
        committed_changes = [
            assistant_pb2.Change(
                file_path="file1.txt",
                change_type="Modified",
                change_content="Content of change 1"
            ),
            assistant_pb2.Change(
                file_path="file2.txt",
                change_type="Added",
                change_content="Content of change 2"
            )
        ]
        uncommitted_changes = [
            assistant_pb2.Change(
                file_path="file1.txt",
                change_type="Modified",
                change_content="Content of uncommitted change 1"
            )
        ]
        recent_edits = "Recent edits to the code go here"
        code_context = assistant_pb2.SmartAutoCompleteRequest.CodeContext(
            current_line="Current line of code",
            previous_lines="Previous lines of code",
            next_lines="Next lines of code"
        )
        repository_url="https://github.com/17-625-API-Design-F23/final-team-project-team-resolvers"
        source_branch="comp3"

        response = smart_auto_complete(repository_url, source_branch, 
                                       committed_changes, uncommitted_changes, 
                                       recent_edits, code_context)
        print(f"response in test is: {response}")
        self.assertIn(response.completion_code, self.sample_data.auto_completion_code_list)

    def test_chat_gpt4_code(self):
        committed_changes = [
            assistant_pb2.Change(
                file_path="file1.txt",
                change_type="Modified",
                change_content="Content of change 1"
            ),
            assistant_pb2.Change(
                file_path="file2.txt",
                change_type="Added",
                change_content="Content of change 2"
            )
        ]
        uncommitted_changes = [
            assistant_pb2.Change(
                file_path="file1.txt",
                change_type="Modified",
                change_content="Content of uncommitted change 1"
            )
        ]
        text_description = "Please help me write a function that calculates the average of a list of numbers."
        repository_url="https://github.com/17-625-API-Design-F23/final-team-project-team-resolvers"
        source_branch="comp3"

        response = chat_gpt4_code(repository_url, source_branch, committed_changes, uncommitted_changes, text_description)
        self.assertIn(response.gpt_response, self.sample_data.gpt_response_list)

    def test_virtual_pair_programming(self):
        # Create a generator of VirtualPairProgrammingRequest
        request_iterator = generate_virtual_pair_programming_requests()  # Implement this function
        
        responses = virtual_pair_programming(request_iterator)
        for response in responses:
            self.assertIn(response.code_pointer[0], self.sample_data.code_pointers_list)
    
if __name__ == '__main__':
    # run all test cases
    unittest.main()
