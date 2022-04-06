from multiprocessing.connection import answer_challenge
import pickle
import xmlrpc
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
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

    # Server function
    def readcsv(name):
        global df
        df = pd.read_csv(name)
        return df.values.tolist()


    def applydf(cond):
        return df.apply(eval(cond)).values.tolist()


    def columns():
        return df.columns.values.tolist()


    def groupby(cond):
        print(type(cond))
        return pickle.dumps(df.groupby(cond))


    def head():
        return df.head(1).values.tolist()


    def isin():
        return pickle.dumps(df.isin([1]))


    def items():
        tuples=[]
        for label, content in df.items():
            tuples.append(content.values.tolist())
        return tuples

    def max(column):
        return str(df[column].max())


    def min(column):
        return str(df[column].min())


    # Adding funtions
    server.register_function(readcsv)
    server.register_function(applydf)
    server.register_function(columns)
    server.register_function(groupby)
    server.register_function(head)
    server.register_function(isin)
    server.register_function(items)
    server.register_function(max)
    server.register_function(min)

    # Run the server's main loop
    server.serve_forever()