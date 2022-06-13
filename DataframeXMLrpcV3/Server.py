from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
import xmlrpc.server
import pickle
import pandas as pd


linkMaster = 'http://localhost:8080'
linkWorker = 'http://localhost:8081'
ID_WORKER = 8081
ID_MASTER = 8080

#Defining Worker class
class Worker(SimpleXMLRPCServer):
        def serve_forever(self):
            #Connecting to the master
            self.workerList = []
            if ( ping(linkMaster) ):
                master_connection = xmlrpc.client.ServerProxy(linkMaster)
                master_connection.addWorker(linkWorker)
                self.quit = 0
            else:
                self.quit = 1
            print("Im a Worker")
            while not self.quit:
                self.handle_request()
                if not ping(linkMaster):
                    self.quit = choose_master()
                else:
                    self.workerList = master_connection.getWorkers()
            return self.quit

#Defining Master class
class Master(SimpleXMLRPCServer):

    def serve_forever(self):
        self.quit = 0
        self.masterWorkerList = worker.workerList
        print("Im a master")
        while not self.quit:
            self.handle_request()
            #pinging workers
            for connection in self.masterWorkerList:
                ping(connection)


#Trying to connect to a distributed component
def ping(connection):
    try:
        workerPing = xmlrpc.client.ServerProxy(connection)
        workerPing.tryConnection()
        established = 1
    except ConnectionRefusedError:
        if (linkMaster != connection):
            worker.workerList.remove(connection)
        established = 0
    return established

#Method to choose a new master in case of failure
def choose_master():
    idMax = str(worker.workerList[0]).split(":")[2]
    for work in worker.workerList:
        id = str(work).split(":")[2]
        idMax = max(id, idMax)
    if idMax == str(ID_WORKER):
        election = 1
        worker.workerList.remove(linkWorker)
    else:
        election = 0
    return election

def tryConnection():
    return 1

def createMaster():
    master = Master(('127.0.0.1', ID_MASTER))
    master.allow_none = True
    master.allow_reuse_port = True
    def addWorker(worker):
        master.masterWorkerList.append(worker)

    def removeWorker(worker):
        worker_remove = xmlrpc.client.ServerProxy(worker)
        worker_remove.kill()
        master.masterWorkerList.remove(worker)

    def getWorkers():
        return master.masterWorkerList

    master.register_function(addWorker)
    master.register_function(removeWorker)
    master.register_function(getWorkers)
    master.register_function(tryConnection)
    return master

#------------------------------------------------WORKER METHODS---------------------------------------------#

# Server dataframe initialized to a selected dataframe
df = pd.read_csv("test1.csv")

#Server functions
def readcsv(name):
    global df
    df = pd.read_csv(name)
    return pickle.dumps(df.values.tolist())

def apply(recived):
    column, cond = str(recived).split(",") 
    return pickle.dumps(df[column].apply(eval(cond)))

def columns():
    return pickle.dumps(df.columns.values.tolist())

def groupby(cond):
    return pickle.dumps(df.groupby([cond]).mean())

def head(num):
    return pickle.dumps(df.head(num))

def isin(item):
    return pickle.dumps(df.isin([item]))

def items():
    tuples=[]
    for label, content in df.items():
        tuples.append(content.values.tolist())
    return pickle.dumps(tuples)

def max(column):
    return pickle.dumps(df[column].max())

def min(column):
    return pickle.dumps(df[column].min())

#Creating worker class
worker = Worker(('127.0.0.1', ID_WORKER))
worker.allow_none = True
worker.allow_reuse_port = True

worker.register_function(readcsv)
worker.register_function(apply)
worker.register_function(columns)
worker.register_function(groupby)
worker.register_function(head)
worker.register_function(isin)
worker.register_function(items)
worker.register_function(max)
worker.register_function(min)
worker.register_function(tryConnection)
#----------------------------------------------------------------------------------------------------------#

if worker.serve_forever():
    master = createMaster()
    master.masterWorkerList = worker.workerList
    master.serve_forever()

