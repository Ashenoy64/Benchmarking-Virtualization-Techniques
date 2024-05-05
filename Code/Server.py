from concurrent import futures
import logging
import math
import time

import grpc
import FileProcess_pb2
import FileProcess_pb2_grpc
import zlib

class FileServerServicer(FileProcess_pb2_grpc.FileProcessingServiceServicer):
    def GetWordCount(self, request, context):
        print(" ---- Word Count ---")
        data = request.content.decode("utf-8")
        words = data.split()
        word_counts = {}
        for word in words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
        return FileProcess_pb2.WordCountResponse(word_counts = [FileProcess_pb2.WordCount(word=word, count=count) for word, count in word_counts.items()])

    def ReadFile(self, request, context):
        print(" --- ReadFile ---")
        CHUNK_SIZE = 1024  
        remaining_data = request.content
        while remaining_data:
            chunk = remaining_data[:CHUNK_SIZE]
            remaining_data = remaining_data[CHUNK_SIZE:]
            compressed_chunk = zlib.compress(chunk, level=zlib.Z_BEST_COMPRESSION)
            print("SENT")
            yield FileProcess_pb2.FileChunk(data=compressed_chunk)

        pass
           

    def UploadFile(self, request_iterator, context):
        print("--- UploadFile ---")
        with open("./ServerData/server_file.txt", "wb") as f:
            for chunk in request_iterator:
                print("RECEIVED")
                f.write(chunk.data)
        
        return FileProcess_pb2.UploadStatus(success = True)



def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    FileProcess_pb2_grpc.add_FileProcessingServiceServicer_to_server(
        FileServerServicer() , server
    )
    server.add_insecure_port("[::]:50051")
    print("Server started on port localhost:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()