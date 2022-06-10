from http import client
import xmlrpc
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import xmlrpc.client


#Class server defining new way of idle
class MyServer(SimpleXMLRPCServer):
    workerList = []
    clientList = []
    def serve_forever(self):
        self.quit = 0
        while True:
            self.handle_request()

#Server functions
def addWorker(worker):
    server.workerList.append(worker)

def removeWorker(worker):
    #Stoping worker execution
    worker_remove = xmlrpc.client.ServerProxy(worker)
    worker_remove.kill()
    server.workerList.remove(worker)

def getWorkers():
    return server.workerList
#Creating server
server = MyServer(('127.0.0.1', 8080))
server.allow_none = True

#Adding functions to the server
server.register_function(addWorker)
server.register_function(removeWorker)
server.register_function(getWorkers)

server.serve_forever()