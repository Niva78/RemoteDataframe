import pickle
import xmlrpc.client

if __name__ == "__main__":

    master = xmlrpc.client.ServerProxy('http://localhost:8080')
    workersList = master.getWorker()
    connections = []
    for worker in workersList:
        connections.append(xmlrpc.client.ServerProxy(worker))

    for connection in connections:
        print("Les connexions disponibles son: ", connection)
        print("---------READ CSV FILE--------------")
        print(connection.readcsv("fitxer.csv"))
        print("---------APPLY--------------")
        print(connection.applydf("lambda x: x**2"))
        print("---------COLUMNS--------------")
        print(connection.columns())
        print("---------GROUPBY--------------")
        print(pickle.loads(connection.groupby('A').data))
        print("---------HEAD--------------")
        print(connection.head())
        print("---------ISIN--------------")
        print(pickle.loads(connection.isin().data))
        print("---------ITEMS--------------")
        print(connection.items())
        print("---------MAX--------------")
        print(pickle.loads(connection.max().data))
        print("---------MIN--------------")
        print(pickle.loads(connection.min().data))

