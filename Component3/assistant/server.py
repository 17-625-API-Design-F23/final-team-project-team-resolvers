"""The Python implementation of the gRPC AIAssistant server by Huanmi."""

import logging
from concurrent import futures
import random

import grpc
import assistant_pb2
import assistant_pb2_grpc

from sample_data import *

class AIAssistantService(assistant_pb2_grpc.AIAssistantServicer):
    def GeneratePRDescription(self, request, context):
        PR_description_list = SampleData().PR_description_list
        PR_description = PR_description_list[random.randint(0, len(PR_description_list) - 1)]
        return assistant_pb2.PRDescriptionResponse(PR_description=PR_description)

    def SmartAutoComplete(self, request, context):
        completion_code_list = SampleData().auto_completion_code_list
        completion_code = completion_code_list[random.randint(0, len(completion_code_list) - 1)]
        return assistant_pb2.SmartAutoCompleteResponse(completion_code=completion_code)
    
    def ChatGPT4Code(self, request, context):
        gpt_response_list = SampleData().gpt_response_list
        gpt_response = gpt_response_list[random.randint(0, len(gpt_response_list) - 1)]
        return assistant_pb2.ChatGPT4CodeResponse(gpt_response=gpt_response)
    
    def generate_code_pointers(self, request):
        # Implement the logic to generate code pointers based on the request
        code_pointers_list = SampleData().code_pointers_list
        # randomly choose three pointers from the list
        indices = random.sample(range(0, len(code_pointers_list) - 1), 3)
        code_pointers = [code_pointers_list[i] for i in indices]
        return code_pointers
        
    def VirtualPairProgramming(self, request_iterator, context):
        for request in request_iterator:
            # Handle the request and generate code pointers
            code_pointers = self.generate_code_pointers(request)

            for code_pointer in code_pointers:
                response = assistant_pb2.VirtualPairProgrammingResponse.CodePointer(
                    delta_code=code_pointer['delta_code'],
                    text_description=code_pointer['text_description']
                )
                yield assistant_pb2.VirtualPairProgrammingResponse(code_pointer=[response])



def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    assistant_pb2_grpc.add_AIAssistantServicer_to_server(AIAssistantService(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print(f"Bithub AI Assistant server started, listening on port {port}")
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()