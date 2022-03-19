import pickle
import xmlrpc.client

import pandas as pd

#PENDIENTE

#Crear lista de workers

#Pedir lista de workers al master

#Cliente ha de propagar la ejecucion de las funciones a los diferentes worker 
#Hacer bucle que envie la funcion a todos los worker disponible

if __name__ == "__main__":
    s = xmlrpc.client.ServerProxy('http://localhost:8080')
    print(s.system.listMethods())

    print("---------LLEGIR FITXER CSV--------------")
    print(s.readcsv("fitxer.csv"))

    print("---------APPLY--------------")
    print(s.applydf("lambda x: x**2"))

    print("---------COLUMNS--------------")
    print(s.columns())

    print("---------GROUPBY--------------")
    print(pickle.loads(s.groupby('A').data))

    print("---------HEAD--------------")
    print(s.head())

    print("---------ISIN--------------")
    print(pickle.loads(s.isin().data))

    print("---------ITEMS--------------")
    print(s.items())

    print("---------MAX--------------")
    print(pickle.loads(s.max().data))

    print("---------MIN--------------")
    print(pickle.loads(s.min().data))

