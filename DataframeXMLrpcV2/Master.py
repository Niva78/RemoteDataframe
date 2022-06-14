import xmlrpc
from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client

from pkg_resources import working_set

            
#Server handler
class MyServer(SimpleXMLRPCServer):
    def serve_forever(self):
        self.quit = 0
        self.workerList = []
        while not self.quit:
            self.handle_request()
            for connection in self.workerList:
                try:
                    connect = xmlrpc.client.ServerProxy(connection)
                    connect.columns()
                except ConnectionRefusedError:
                    print("Muerto")
                    self.workerList.remove(connection)
                    print(self.workerList)

# Funtion definition
def addWorker(worker):
    server.workerList.append(worker)

def removeWorker(worker):
    #Stoping worker execution
    worker_remove = xmlrpc.client.ServerProxy(worker)
    worker_remove.kill()
    server.workerList.remove(worker)

def getWorkers():
    return server.workerList

server = MyServer(('127.0.0.1', 8080))  
server.allow_none = True


# Adding functions
server.register_function(addWorker)
server.register_function(removeWorker)
server.register_function(getWorkers)

# Run the server's main loop
server.serve_forever()
