from YelpQueueNode import YelpQueueNode
from YelpQueue import YelpQueue

node1 = YelpQueueNode("Taryn", None)
node2 = YelpQueueNode("Michael", None)
node3 = YelpQueueNode("Lila", None)

node2.setNext(node1)
node3.setNext(node2)

queue = YelpQueue([])
queue.buildQueue(node1)

queue.enqueue(node3)
queue.printQueue()