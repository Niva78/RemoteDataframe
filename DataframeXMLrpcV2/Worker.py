import pickle
import xmlrpc
from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
import pandas as pd



#Server handler
class MyServer(SimpleXMLRPCServer):
    def serve_forever(self):
        self.quit = 0
        while not self.quit:
            self.handle_request()


#Connecting to server
s = xmlrpc.client.ServerProxy('http://localhost:8080')

#Adding worker to master
s.addWorker('http://localhost:8090')

# Server dataframe initialized to empty dataframe
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

def kill():
    server.quit = 1
    return 1


#Creating server
server = MyServer(('127.0.0.1', 8091))  
server.allow_none = True

# Adding funtions
server.register_function(readcsv)
server.register_function(apply)
server.register_function(columns)
server.register_function(groupby)
server.register_function(head)
server.register_function(isin)
server.register_function(items)
server.register_function(max)
server.register_function(min)
server.register_function(kill)

# Run the server's main loop
server.serve_forever()


#This way we can remove a worker from the system
#master.removeWorker('http://localhost:8090')