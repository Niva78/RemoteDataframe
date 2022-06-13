from time import time
import xmlrpc.client
import time


master = xmlrpc.client.ServerProxy('http://localhost:8080')
print(master.getWorkers())

