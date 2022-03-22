class Master():
    # Master variables
    workerslist = []

    # Funtion definition
    def addWorkers(self, worker):
        self.workerslist.append(worker)

    def removeWorker(self, worker):
        return self.workerslist.remove(worker)

    def getWorkers(self):
        return self.workerslist

