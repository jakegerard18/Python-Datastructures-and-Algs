from LinkedList import *

class Queue:
    def __init__(self, startingNode = None):
        self.queue = LinkedList(startingNode)
        if startingNode is None:
            self.size = 0
            return
        self.size = 1

    def enque(self, node):
        if type(node) is not Node:
            node = Node(node)
        if self.queue.getSize() == 0:
            self.queue.addToHead(node)
        else:
            self.queue.addToTail(node)

        self.size += 1

    def deque(self):
        self.size -= 1
        return self.queue.removeHead()

    def getSize(self):
        return self.size

    def printQueue(self):
        self.queue.printList()