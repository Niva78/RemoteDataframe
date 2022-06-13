import xmlrpc
from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client

            
#Server handler
class MyServer(SimpleXMLRPCServer):
    workerslist = []
    def serve_forever(self):
        self.quit = 0
        while not self.quit:
            self.handle_request()
            for connection in self.workerslist:
                try:
                    connect = xmlrpc.client.ServerProxy(connection)
                    connect.columns()
                except ConnectionRefusedError:
                    self.workerslist.remove(connection)

# Funtion definition
def addWorker(worker):
    server.workerslist.append(worker)

def removeWorker(worker):
    global workerslist
    #Stoping worker execution
    worker_remove = xmlrpc.client.ServerProxy(worker)
    worker_remove.kill()
    server.workerslist.remove(worker)
    print(workerslist)

def getWorkers():
    return server.workerslist

server = MyServer(('127.0.0.1', 8080))  
server.allow_none = True


# Adding functions
server.register_function(addWorker)
server.register_function(removeWorker)
server.register_function(getWorkers)

# Run the server's main loop
server.serve_forever()
