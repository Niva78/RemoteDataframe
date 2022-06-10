from http import client
import xmlrpc
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import xmlrpc.client
import pickle

class MyServer(SimpleXMLRPCServer):
    workerList = []
    clientList = []
    def serve_forever(self):
        self.quit = 0
        while not self.quit:
            #Connecting to master
            master = xmlrpc.client.ServerProxy('http://localhost:8080')

            #Getting workers
            self.workersList = master.getWorkers()
            self.connections = []
            for worker in self.workersList:
                self.connections.append(xmlrpc.client.ServerProxy(worker))

            #Proving read csv function
            for worker in self.connections:
                print(pickle.loads(worker.readcsv("test1.csv").data))

            #Proving apply function
            for worker in self.connections:
                print(pickle.loads(worker.apply("Payment,lambda x:x**2").data))

            #Proving columns function
            for worker in self.connections:
                print(pickle.loads(worker.columns().data))

            #Proving groupby function
            for worker in self.connections:
                print(pickle.loads(worker.groupby("Name").data))

            #Proving head function
            for worker in self.connections:
                print(pickle.loads(worker.head(3).data))

            #Proving isin function
            for worker in self.connections:
                print(pickle.loads(worker.isin("Nico").data))

            #Proving items function
            for worker in self.connections:
                print(pickle.loads(worker.items().data))

            #Proving max function
            for worker in self.connections:
                print(pickle.loads(worker.max("Payment").data))

            #Proving min function
            for worker in self.connections:
                print(pickle.loads(worker.min("Payment").data))
            server.handle_request()


def kill():
    server.quit = 1
    return 1

server = MyServer(('127.0.0.1', 8091))  
server.allow_none = True
server.serve_forever()