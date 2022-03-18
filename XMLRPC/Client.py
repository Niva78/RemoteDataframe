import xmlrpc.client

import pandas as pd

#PENDIENTE

#Crear lista de workers

#Pedir lista de workers al master

#Cliente ha de propagar la ejecucion de las funciones a los diferentes worker 
#Hacer bucle que envie la funcion a todos los worker disponible

if __name__ == "__main__":
    # s = xmlrpc.client.ServerProxy('http://localhost:8000')
    s = xmlrpc.client.ServerProxy('http://localhost:8080')
    print(s.system.listMethods())
    print(s.getinsult())

    print("---------LLEGIR FITXER CSV--------------")
    #print(s.readcsv())

    print("---------APPLY--------------")
    #print(s.applydf("lambda x: x**2"))

    print("---------COLUMNS--------------")
    #print(s.columns())

    print("---------GROUPBY--------------")
    print(s.groupby("A"))

    print("---------HEAD--------------")
    print(s.head())

    print("---------ISIN--------------")
    print(s.isin())

    print("---------ITEMS--------------")
    #print(s.items())

    print("---------MAX--------------")
    print(s.max())

    print("---------MIN--------------")
    print(s.min())

