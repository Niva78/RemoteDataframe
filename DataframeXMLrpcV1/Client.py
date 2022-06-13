import pickle
import xmlrpc.client

#Connecting to master
master = xmlrpc.client.ServerProxy('http://localhost:8080')

#Getting workers
workersList = master.getWorker()
connections = []
for worker in workersList:
    connections.append(xmlrpc.client.ServerProxy(worker))

#Proving workers

#Proving read csv function
for worker in connections:
    print(pickle.loads(worker.readcsv("test1.csv").data))

#Proving apply function
for worker in connections:
    print(pickle.loads(worker.apply("Payment,lambda x:x**2").data))

#Proving columns function
for worker in connections:
    print(pickle.loads(worker.columns().data))

#Proving groupby function
for worker in connections:
    print(pickle.loads(worker.groupby("Name").data))

#Proving head function
for worker in connections:
    print(pickle.loads(worker.head(3).data))

#Proving isin function
for worker in connections:
    print(pickle.loads(worker.isin("Nico").data))

#Proving items function
for worker in connections:
    print(pickle.loads(worker.items().data))

#Proving max function
for worker in connections:
    print(pickle.loads(worker.max("Payment").data))

#Proving min function
for worker in connections:
    print(pickle.loads(worker.min("Payment").data))