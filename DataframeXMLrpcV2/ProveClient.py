from doctest import master
import xmlrpc.client

master = xmlrpc.client.ServerProxy('http://localhost:8080')

master.addWorker("Buenas")
workers = master.getWorkers()

print(workers)