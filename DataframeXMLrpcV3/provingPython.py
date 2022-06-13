import xmlrpc
from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client



def ping(connection):
    try:
        connection.kill()
        print("Buenas")
    except ConnectionRefusedError:
        print("Adios")


master = xmlrpc.client.ServerProxy('http://localhost:8080')

ping(master)
