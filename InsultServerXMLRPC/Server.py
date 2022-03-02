from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import random

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


# Create server
with SimpleXMLRPCServer(('10.112.150.234', 2051), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    #Server variables
    list1 = ["bajoca", "putero", "tonto", "Romaní"]



    # Funtion definition
    def addInsult(insult):
        list1.append(insult)
        return 0
    
    def getInsult():
        return list1
    
    def insultme():
        return list1[random.randint(0, len(list1))]


    #Adding funtions 
    server.register_function(addInsult)
    server.register_function(getInsult)
    server.register_function(insultme)

    # Run the server's main loop
    server.serve_forever()