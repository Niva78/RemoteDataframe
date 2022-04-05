from urllib import response
import grpc
from concurrent import futures
import time

#Import generated classes
import APIDataframe_pb2
import APIDataframe_pb2_grpc

#Import orginall class
import APIDataframe

#Generate a derived class from ...grpc.Servicer
class APIDataframeServicer(APIDataframe_pb2_grpc.APIDataframeServicer):
    
    #Funtion definition
    def Min(self, request, context):
        response = APIDataframe_pb2.Result()
        response.result = APIDataframe.min()
        return response
    
    #Funtion definition
    def Max(self, request, context):
        response = APIDataframe_pb2.Result()
        response.result = APIDataframe.max()
        return response


#Creating grpc server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

#Adding the function to the server
APIDataframe_pb2_grpc.add_APIDataframeServicer_to_server(APIDataframeServicer(), server)

#Listening on port
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

#Infinite loop
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)