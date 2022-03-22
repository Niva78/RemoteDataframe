import pickle
import xmlrpc.client
<<<<<<< HEAD
import pandas as pd

if __name__ == "__main__":
    urlPort = 'http://localhost:8090'
    urlPort2 = 'http://localhost:8080'
    urlPort3 = 'http://localhost:8081'
    s = xmlrpc.client.ServerProxy(urlPort)
    s2 = xmlrpc.client.ServerProxy(urlPort2)
    s3 = xmlrpc.client.ServerProxy(urlPort3)
    split = urlPort.split(":")
    split2 = urlPort2.split(":")
    split3 = urlPort3.split(":")
    worker = split[2]
    worker2 = split2[2]
    worker3 = split3[2]

    master = Master()

    print("---------ADD WORKER TO MASTER--------------")
    master.addWorkers(worker)
    master.addWorkers(worker2)
    master.addWorkers(worker3)

    print("---------GET WORKERS--------------")
    print(master.getWorkers())

    workersList = master.getWorkers()
    
    print("---------READ CSV FILE--------------")
    print(s.readcsv("fitxer.csv"))
    print(s2.readcsv("fitxer2.csv"))
    print(s3.readcsv("fitxer3.csv"))

    print("---------APPLY--------------")
    print(s.applydf("lambda x: x**2"))
    print(s2.applydf("lambda x: x**2"))
    print(s3.applydf("lambda x: x**2"))

    print("---------COLUMNS--------------")
    print(s.columns())
    print(s2.columns())
    print(s3.columns())

    print("---------GROUPBY--------------")
    print(pickle.loads(s.groupby('A').data))
    print(pickle.loads(s2.groupby('A').data))
    print(pickle.loads(s3.groupby('A').data))

    print("---------HEAD--------------")
    print(s.head())
    print(s2.head())
    print(s3.head())

    print("---------ISIN--------------")
    print(pickle.loads(s.isin().data))
    print(pickle.loads(s2.isin().data))
    print(pickle.loads(s3.isin().data))

    print("---------ITEMS--------------")
    print(s.items())
    print(s2.items())
    print(s3.items())

    print("---------MAX--------------")
    print(pickle.loads(s.max().data))
    print(pickle.loads(s2.max().data))
    print(pickle.loads(s3.max().data))
=======


if __name__ == "__main__":
>>>>>>> 5fb7203121838556c152daffdfb29dbe2bab2eb9

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
