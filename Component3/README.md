# AI Assistant for Bithub

## 1 API Selection
For the AI Assistant component, I choose gRPC. The rationale behind is as follows:
* Performance Efficiency: HTTP/2
* Data Serialization: Protocol buffers is more efficient and compact
* Strongly-typed Contracts
* Streaming Capabilities
* Scalability

## 2 Design
### 2.1 Protocol Buffers
- **Message Definitions**: Messages for request and response are defined for each functionality. For example, a `PRDescriptionRequest` message may contain fields like `repository_url` and `branch_name`, and a `PRDescriptionResponse` message may contain a `description` field.
- **Service Definition**: The AI Assistant service is defined with RPC methods corresponding to each functionality. Each method specifies its request and response message types.

### 2.2 gRPC Services
- **Service Implementation**: Each service method, such as `GeneratePRDescription`, is implemented to process the incoming request and generate a response. This implementation includes mock logic for the AI assistant's functionalities.
- **Server Setup**: The server is configured to handle incoming RPC calls and dispatch them to the appropriate service methods.

### 2.3 Server Stubs
- **Stub Configuration**: The server stubs are set up to listen on a specified port and create instances of the service implementation.
- **Request Handling**: The server stubs handle requests by invoking the corresponding service method and sending back responses.


### 2.4 Client Stubs
- **Stub Initialization**: Client stubs are initialized with the server's address and port information.
- **Method Invocation**: For each functionality, the client stub invokes the corresponding RPC method on the server, passing in the required request message and receiving a response.

### 2.5 Unit Test Cases
tbc

## 3 Implementation
```sh
source grpc/bin/activate
deactivate
```