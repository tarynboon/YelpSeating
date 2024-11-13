
class YelpQueueNode():
    def __init__(self, name, next):
        self.name = name
        self.next = next

    def getName(self):
        return self.name

    def getNext(self):
        return self.next

    def setNext(self, next):
        self.next = next

    def setName(self, name):
        self.name = name