from LinkedList import LinkedList

class Queue:
    def __init__(self, startingNode):
        self.queue = LinkedList(startingNode)

    def enque(self, node):
        self.queue.addToTail(node)

    def deque(self):
        return self.queue.removeHead()

    def printQueue(self):
        self.queue.printList()