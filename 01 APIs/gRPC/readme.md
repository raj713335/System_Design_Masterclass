A **basic gRPC example in Python**, including:

1. Defining a service in a `.proto` file
2. Generating Python code from the `.proto`
3. Writing the server
4. Writing the client

---

### 📁 Folder structure:

```
grpc_example/
├── greet.proto
├── greeter_server.py
├── greeter_client.py
```

---

## 1. `greet.proto` (Defining the gRPC service)

```proto
syntax = "proto3";

package greet;

// The greeting service definition.
service Greeter {
  // Sends a greeting
  rpc SayHello (HelloRequest) returns (HelloReply) {}
}

// The request message containing the user's name.
message HelloRequest {
  string name = 1;
}

// The response message containing the greetings.
message HelloReply {
  string message = 1;
}
```

---

## 2. Generate Python gRPC code from `.proto`

Install required packages:

```bash
pip install grpcio grpcio-tools
```

Then generate the code:

```bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. greet.proto
```

This creates:

* `greet_pb2.py`
* `greet_pb2_grpc.py`

---

## 3. `greeter_server.py` (gRPC Server)

```python
import grpc
from concurrent import futures
import time
import greet_pb2
import greet_pb2_grpc

class GreeterServicer(greet_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return greet_pb2.HelloReply(message=f"Hello, {request.name}!")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greet_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started on port 50051.")
    try:
        while True:
            time.sleep(86400)  # 1 day
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
```

---

## 4. `greeter_client.py` (gRPC Client)

```python
import grpc
import greet_pb2
import greet_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = greet_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(greet_pb2.HelloRequest(name='Alice'))
    print("Greeter client received:", response.message)

if __name__ == '__main__':
    run()
```

---

## ✅ Run it

1. Start the server in one terminal:

```bash
python greeter_server.py
```

2. Run the client in another terminal:

```bash
python greeter_client.py
```

---
