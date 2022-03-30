from unittest import result
import grpc

# import the generated classes
import min_pb2
import min_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = min_pb2_grpc.MinStub(channel)

# create a valid request message
number = min_pb2.Result(result=None)

# make the call
response = stub.min(number)

# et voilà
print(response.result)