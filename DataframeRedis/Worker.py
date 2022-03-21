from asyncio.windows_events import NULL
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import pandas as pd
import redis

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

print("Creating new worker...")

# Create server
with SimpleXMLRPCServer(('localhost', 8081), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    #Connecting worker to master
    redis_cli = redis.Redis(host="localhost", port=6379)
    #Adding his URL to the master
    redis_cli.append('URL', 'localhost')
    print(str(redis_cli.get('URL')))

    # Server dataframe initialized to empty dataframe
    df = pd.DataFrame({'A' : []})

    #Server function
    def readcsv(name):
        df = pd.read_csv(name)
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
