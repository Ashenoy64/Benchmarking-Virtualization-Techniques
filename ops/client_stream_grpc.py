import grpc
import your_service_pb2
import your_service_pb2_grpc

# Define the server address and port
server_address = 'localhost'
server_port = '50051'

# Create a gRPC channel and stub
channel = grpc.insecure_channel(f'{server_address}:{server_port}')
stub = your_service_pb2_grpc.YourServiceStub(channel)

def client_streaming_call():
    # Prepare a list of request messages
    requests = [
        your_service_pb2.YourRequest(
            # Add your request data here
        ),
        your_service_pb2.YourRequest(
            # Add your request data here
        ),
        # Add more requests as needed
    ]

    # Make the client streaming call
    responses = stub.YourClientStreamingRPC(iter(requests))

    # Iterate over responses
    for response in responses:
        # Handle the response
        # You can access the response fields like response.field_name
        print("Received:", response)

if __name__ == '__main__':
    client_streaming_call()
