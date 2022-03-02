import xmlrpc.client

#s = xmlrpc.client.ServerProxy('http://localhost:8000')
s = xmlrpc.client.ServerProxy('http://10.21.4.0:8080')
print(s.system.listMethods())
#print(s.getInsults())

