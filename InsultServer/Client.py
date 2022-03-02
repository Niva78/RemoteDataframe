import xmlrpc.client

#s = xmlrpc.client.ServerProxy('http://localhost:8000')
s = xmlrpc.client.ServerProxy('http://10.112.146.179:8000')
print(s.system.listMethods())
s.addInsult("Perro")
print(s.getInsults())

