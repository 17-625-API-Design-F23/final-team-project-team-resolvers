# AI Assistant for Bithub

## 1 API Selection
For the AI Assistant component, I choose gRPC. The rationale behind is as follows:
* Performance Efficiency: HTTP/2
* Data Serialization: Protocol buffers is more efficient and compact
* Strongly-typed Contracts
* Streaming Capabilities
* Scalability

## 2 Design

### 2.1 gRPC Services
- Purpose: The gRPC service for the AI assistant is designed to facilitate various functionalities such as generating PR descriptions, code completions, and providing conversational programming support.
- Service Name: AIAssistantService
- Description: This service encapsulates the core functionalities of the AI assistant, providing an interface for clients to interact with the AI capabilities.

### 2.2 Protocol Buffers
- **Message Definitions**: Messages for request and response are defined for each functionality. For example, a `PRDescriptionRequest` message may contain fields like `repository_url` and `branch_name`, and a `PRDescriptionResponse` message may contain a `description` field.
- **Service Definition**: The AI Assistant service is defined with RPC methods corresponding to each functionality. Each method specifies its request and response message types.

```
message PRDescriptionRequest {
    string repository_url = 1;
    string branch_name = 2;
}
```

### 2.3 Server Contracts
- Method: GeneratePRDescription
	- Input Parameters: PRDescriptionRequest, containing fields like repository_url and branch_name.
	- Return Type: PRDescriptionResponse, containing a description string.

- Method: ProvideCodeCompletion
	- Input Parameters: CodeCompletionRequest, with fields defining the current coding context.
	- Return Type: CodeCompletionResponse, including suggested code completions.

- Method: GenerateCodeFromDescription
	- Input Parameters: CodeGenerationRequest, containing a task description in natural language.
	- Return Type: CodeGenerationResponse, with a generated code snippet.

- Method: VirtualPairProgramming
	- Input Parameters: PairProgrammingRequest, including details of the coding problem or query.
	- Return Type: PairProgrammingResponse, providing code suggestions or solutions.


### 2.4 Unit Test Cases
tbc

## 3 Implementation
### 3.1 Environment
Build in the virtual environment.
```sh
cd Component3
python -m venv grpc_env
source grpc_env/bin/activate
pip install -r requirements.txt
# for exiting the env:
# deactivate
```
In Component3, define the proto in `protos/assistant.proto` and generate gRPC code using:
```sh
python -m grpc_tools.protoc -I./protos --python_out=./assistant --pyi_out=./assistant --grpc_python_out=./assistant ./protos/assistant.proto
```