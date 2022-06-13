from multiprocessing.connection import answer_challenge
import pickle
import xmlrpc
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
from numpy import average
import pandas as pd


# Restrict to a particular path.


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


# Create server
with SimpleXMLRPCServer(('localhost', 8090), requestHandler=RequestHandler, allow_none=True) as server:
    server.register_introspection_functions()

    s = xmlrpc.client.ServerProxy('http://localhost:8080')
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

    # Run the server's main loop
    server.serve_forever()
