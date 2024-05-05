from __future__ import print_function

import logging
import random

import grpc
import FileProcess_pb2
import FileProcess_pb2_grpc


def word_count(stub):
    with open('data_client.txt', 'rb') as f:
        data = f.read()
    request = FileProcess_pb2.File(filename="data_client.txt",content = data)
    response = stub.GetWordCount(request)

    for i in response.word_counts:
        print(i.word," : ", i.count)


def compress_file(stub):
    with open('data_client.txt', 'rb') as f:
        data = f.read()
    request = FileProcess_pb2.File(filename="data_client.txt",content = data)
    response = stub.ReadFile(request)

    with open("compressed_data.txt", "wb") as f:
        for chunk in response:
            f.write(chunk.data)

def upload_file(stub):
    with open("data_client.txt", "rb") as f:
        data = f.read()
        
    chunks = [data[i:i+1024] for i in range(0, len(data), 1024)]
    request_iterator = (FileProcess_pb2.FileChunk(data=chunk) for chunk in chunks)
    response = stub.UploadFile(request_iterator)
    print(response.success)

def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = FileProcess_pb2_grpc.FileProcessingServiceStub(channel)
        #word_count(stub)
        #compress_file(stub)
        upload_file(stub)
        
        
        

if __name__ == "__main__":
    logging.basicConfig()
    run()