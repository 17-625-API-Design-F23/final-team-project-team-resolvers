"""The Python implementation of the gRPC AIAssistant client by Huanmi."""

from __future__ import print_function

import logging

import grpc
import assistant_pb2
import assistant_pb2_grpc

def get_pr_description(repository_url, branch_name, committed_changes) -> assistant_pb2.PRDescriptionResponse:
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = assistant_pb2_grpc.AIAssistantStub(channel)
        response = stub.GeneratePRDescription(assistant_pb2.PRDescriptionRequest(
            repository_url=repository_url, 
            source_branch=branch_name,
            committed_changes=committed_changes,
            )
        )

    print(f"PR description generated by our AI Assistant: {'\n'}{response.PR_description}")
    return response

def smart_auto_complete(
        repository_url, branch_name, committed_changes, 
        uncommitted_changes, recent_edits, code_context) \
        -> assistant_pb2.SmartAutoCompleteResponse:
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = assistant_pb2_grpc.AIAssistantStub(channel)
        response = stub.SmartAutoComplete(assistant_pb2.SmartAutoCompleteRequest(
            repository_url=repository_url,
            branch_name=branch_name,
            committed_changes=committed_changes,
            uncommitted_changes=uncommitted_changes,
            recent_edits=recent_edits,
            code_context= code_context
        ))

    print(f"Completion code generated by our AI Assistant: {'\n'}{response.completion_code}")
    return response

def send_one_chat_gpt4_code_request(repository_url, branch_name, committed_changes, uncommitted_changes, text_description):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = assistant_pb2_grpc.AIAssistantStub(channel)

        response = stub.ChatGPT4Code(assistant_pb2.ChatGPT4CodeRequest(
            repository_url=repository_url,
            branch_name=branch_name,
            committed_changes=committed_changes,
            uncommitted_changes=uncommitted_changes,
            text_description=text_description
        
        ))
    return response

def chat_gpt4_code(repository_url, branch_name, committed_changes, uncommitted_changes, text_description) -> assistant_pb2.ChatGPT4CodeResponse:  
    response = send_one_chat_gpt4_code_request(
        repository_url=repository_url,
        branch_name=branch_name,
        committed_changes=committed_changes,
        uncommitted_changes=uncommitted_changes,
        text_description=text_description
    )
    
    # Check if the server asks for clarification
    while (response.gpt_response == "Needs clarification on your description! Please provide more details."):
        print(f"Server asks for clarification. Please send a new request with more details. {'\n'}")
        new_text_description = "Please help me write a function that calculates the average of a list of numbers. The list of numbers is [1, 2, 3, 4, 5]."
        response = send_one_chat_gpt4_code_request(
            repository_url=repository_url,
            branch_name=branch_name,
            committed_changes=committed_changes,
            uncommitted_changes=uncommitted_changes,
            text_description=new_text_description
        )
    
    print(f"Code generated by ChatGPT: {'\n'}{response}")
    return response

def generate_virtual_pair_programming_requests():
    uncommitted_changes = [
        assistant_pb2.Change(
            file_path="file1.txt",
            change_type="Modified",
            change_content= """
    def factorial(n):
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    number = 5
    fact = factorial(number)
    print(f"The factorial of {number} is {fact}")
                            """
        )
    ]
    request = assistant_pb2.VirtualPairProgrammingRequest(
        repository_url="https://github.com/17-625-API-Design-F23/final-team-project-team-resolvers",
        branch_name="comp3",
        uncommitted_changes=uncommitted_changes,
        text_description="Could you help me check if there is any bug in this loop I just wrote?"
    )
    
    # put 10 request in requests
    requests = [request] * 10
    for request in requests:
        yield assistant_pb2.VirtualPairProgrammingRequest(
            repository_url=request.repository_url,
            branch_name=request.branch_name,
            uncommitted_changes=request.uncommitted_changes,
            text_description=request.text_description
        )

def handle_vpp_response(response):
    print(f"Code pointers received from the server: {'\n'}")
    code_pointers = response.code_pointer
    for code_pointer in code_pointers:
        print(f"Delta_code: {'\n'} {code_pointer.delta_code} {'\n'}" \
               f"Text_description: {'\n'} {code_pointer.text_description} {'\n\n'}"
            )

def virtual_pair_programming(request_iterator) -> assistant_pb2.VirtualPairProgrammingResponse:
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = assistant_pb2_grpc.AIAssistantStub(channel)
        # Make the bidirectional streaming RPC call
        responses = stub.VirtualPairProgramming(request_iterator)

        for response in responses:
            # Handle the VirtualPairProgrammingResponse
            handle_vpp_response(response)  # Implement this function
        
        return responses



if __name__ == '__main__':
    logging.basicConfig()
    # take input from terminal to choose which function to run
    print("""Please choose which function to run: 
    1. Generate PR description
    2. Smart auto complete
    3. Chat GPT4 code
    4. Virtual pair programming
    """)
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

    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            get_pr_description(repository_url, source_branch, committed_changes)
            break
        elif choice == "2":
            smart_auto_complete()
            break
        elif choice == "3":
            chat_gpt4_code()
            break
        elif choice == "4":
            virtual_pair_programming()
            break
        else:
            print("Invalid input. Please try again.")
