"""The Python implementation of the gRPC AIAssistant client by Huanmi."""

from __future__ import print_function

import logging

import grpc
import assistant_pb2
import assistant_pb2_grpc

def get_pr_description():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = assistant_pb2_grpc.AIAssistantStub(channel)
        response = stub.GeneratePRDescription(assistant_pb2.PRDescriptionRequest(
            repository_url="https://github.com/17-625-API-Design-F23/final-team-project-team-resolvers", 
            branch_name="main",
            committed_code="committed code",
            )
        )

    print("AI Assistant response: " + response.PR_description)


if __name__ == '__main__':
    logging.basicConfig()
    get_pr_description()