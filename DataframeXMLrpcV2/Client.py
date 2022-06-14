from time import time
import xmlrpc.client
import time


#We implement a pull system in which client call master in order to update the worker list
def update_workers(master):
    workersList = master.getWorkers()
    connections = []
    for worker in workersList:
        connections.append(xmlrpc.client.ServerProxy(worker))
    return connections

#Connecting to master
master = xmlrpc.client.ServerProxy('http://localhost:8080')

#Proving read csv function
connections = update_workers(master)

print("Antes")
print(connections)
master.removeWorker("http://localhost:8092")
time.sleep(4)

connections = update_workers(master)

time.sleep(4)
print("Despues")
print(connections)