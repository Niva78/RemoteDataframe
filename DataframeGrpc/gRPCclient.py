from unittest import result
import grpc

import APIDataframe_pb2
import APIDataframe_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')

#Create a stub or a client
stub = APIDataframe_pb2_grpc.APIDataframeStub(channel)

#create valid request message
number = APIDataframe_pb2.Result(result=bytes(1))

#calling server
response = stub.Min(number)

print(response.result)