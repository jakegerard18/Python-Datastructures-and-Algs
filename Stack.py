from LinkedList import LinkedList

class Stack:
    def __init__(self, startingNode):
        self.size = 0
        self.stack = LinkedList(startingNode)

    def push(self, node):
        self.stack.addToHead(node)
        self.size += 1

    def pop(self):
        self.size -= 1
        return self.stack.removeHead()

    def peak(self):
        return self.stack.getHead()

    def printStack(self):
        self.stack.printList()

