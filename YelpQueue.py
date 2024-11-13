from YelpQueueNode import YelpQueueNode

class YelpQueue():
    def __init__(self, namesList):
        self.queue = None
        for name in namesList:
            self.enqueue(name)

    def printQueue(self):
        pointer = self.queue

        while pointer is not None:
            print(pointer.getName())
            pointer = pointer.getNext()

    def buildQueue(self, queue):
        self.queue = queue

    def enqueue(self, name):
        newCustomer = YelpQueueNode(name, None)
        if(self.queue is None):
            self.queue = newCustomer
        else:
            newCustomer.setNext(self.queue)

    def seat(self):
        pointer = self.queue
        if pointer is None:
            print("no customers")
        else:
            previous = None
            while pointer.getNext() is not None:
                previous = pointer
                pointer = pointer.getNext()
            previous.setNext(None)
            print("seating", pointer.getName())

    def remove(self, queue):
        next = queue.getNext()
        queue.setNext(next)
        queue.remove(self)
