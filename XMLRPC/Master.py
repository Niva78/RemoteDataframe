import xmlrpc
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = '/RPC2'


with SimpleXMLRPCServer(('localhost', 8080), requestHandler=RequestHandler, allow_none=True) as server:
    server.register_introspection_functions()

    # Master variables
    workerslist = []

    # Funtion definition
    def addWorker(worker):
        global workerslist
        workerslist.append(worker)


    def removeWorker(worker):
        global workerslist
        workerslist.remove(worker)


    def getWorker():
        return workerslist

    # Adding functions
    server.register_function(addWorker)
    server.register_function(removeWorker)
    server.register_function(getWorker)

    # Run the server's main loop
    server.serve_forever()
