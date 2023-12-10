# AI Assistant for Bithub

## 1 Introduction
This folder implements Component3 using gRPC. The folder structure is:
```
Component3/
├── assistant/
│   ├── assistant_pb2_grpc.py
│   ├── assistant_pb2.py
│   ├── assistant_pb2.pyi
│   ├── client.py
│   ├── sample_data.py
│   ├── server.py
│   └── test.py
├── grpc/
├── protos/
│   └── assistant.proto
├── README.md
├── requirements.txt
└── .gitignore
```
Definition of proto is in `protos/assistant.proto`. gRPC Services and server stubs are in `assistant/server.py` and client stubs are in `assistant/client.py`. Unit tests are in `assistant/test.py`.

## 2 Setup
### 2.1 Environment
Build in the virtual environment.
```sh
# perform in Component3
python -m venv grpc_env
source grpc_env/bin/activate
pip install -r requirements.txt
# for exiting the env:
# deactivate
```
### 2.2 Generate gRPC code:
In Component3, define the proto in `protos/assistant.proto` and generate gRPC code using:
```sh
python -m grpc_tools.protoc -I./protos --python_out=./assistant --pyi_out=./assistant --grpc_python_out=./assistant ./protos/assistant.proto
```

### 2.3 Run Server/Client
Run with:
```sh
python assistant/server.py
python assistant/client.py 
```

### 2.4 Run unit tests
Run with server on, then run:
```sh
python assistant/test.py
```