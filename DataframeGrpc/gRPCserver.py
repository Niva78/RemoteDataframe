import grpc
from concurrent import futures
import time
import pandas as pd

# import the generated classes
import min_pb2
import min_pb2_grpc

# import the original calculator.py
import min

# create a class to define the server functions, derived from
# calculator_pb2_grpc.CalculatorServicer
class MinServicer(min_pb2_grpc.MinServicer):
    dataframe = pd.read_csv("test1.csv")
    # calculator.square_root is exposed here
    # the request and response are of the data type
    # calculator_pb2.Number
    def min(self, request, context):
        response = min_pb2.Result()
        response.result = self.dataframe.min()#min.min(None)
        return response


# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function `add_CalculatorServicer_to_server`
# to add the defined class to the server
min_pb2_grpc.add_MinServicer_to_server(
        MinServicer(), server)

# listen on port 50051
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)