import pickle
import xmlrpc.client


master = xmlrpc.client.ServerProxy('http://localhost:8080')
workersList = master.getWorker()
connections = []
for worker in workersList:
    connections.append(xmlrpc.client.ServerProxy(worker))


#Proving max function
for worker in connections:
    print (worker.max("Name"))

#Proving groupby function
for worker in connections:
    print(pickle.loads(worker.groupby("Name")))