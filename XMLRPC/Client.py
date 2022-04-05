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
        print(pickle.loads(connection.isin(1).data))
        print("---------ITEMS--------------")
        print(connection.items())
        print("---------MAX--------------")
        print(pickle.loads(connection.max().data))
        valor = pickle.loads(connection.max().data)
        if (max == None and max < valor):
            max = valor
        print("The maximum worker's value is: ",max)

        print("---------MIN--------------")
        print(pickle.loads(connection.min().data))
        valor = pickle.loads(connection.min().data)
        if (min == None and min < valor):
            min = valor

        print("The minimum worker's value is: ", min)
