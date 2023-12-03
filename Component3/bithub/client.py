import grpc
import bithub_pb2
import bithub_pb2_grpc

def get_pr_description(repository_url, branch_name):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = bithub_pb2_grpc.AIAssistantStub(channel)
        response = stub.GeneratePRDescription(bithub_pb2.PRDescriptionRequest(repository_url=repository_url, branch_name=branch_name))
    print("AI Assistant response: " + response.description)
