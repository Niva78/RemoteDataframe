from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import random
import pandas as pd
from csv import reader


# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


# Create server
with SimpleXMLRPCServer(('localhost', 8080), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()
    # Server variables
    list1 = ["bajoca", "putero", "tonto", "Romaní"]
    df = pd.read_csv('fitxer.csv')
    print(df)


    # Funtion definition
    def addinsult(insult):
        list1.append(insult)
        return 0


    def getinsult():
        return list1


    def insultme():
        return list1[random.randint(0, len(list1))]


    def readcsv():
        return df.values.tolist()


    def applydf(cond):
        return df.apply(eval(cond)).values.tolist()


    def columns():
        return df.columns.values.tolist()


    def groupby(cond):
        return df.groupby([cond]).mean()

    def head():
        return df.head(1).values.tolist()


    def isin():
        return df.isdin(1).values.tolist()


    # def items():
    # for label, content in df.items():
    #     print('label:', label)
    #     print('content:', content, sep='\n')

    def max():
        return df.max.values.tolist()


    def min():
        return df.min.values.tolist()


    # Adding funtions
    server.register_function(addinsult)
    server.register_function(getinsult)
    server.register_function(insultme)
    server.register_function(readcsv)
    server.register_function(applydf)
    server.register_function(columns)
    server.register_function(groupby)
    server.register_function(head)
    server.register_function(isin)
    # server.register_function(items())
    server.register_function(max)
    server.register_function(min)

    # Run the server's main loop
    server.serve_forever()
