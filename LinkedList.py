from Node import Node

class LinkedList:
    def __init__(self, startingNode):
        self.head = startingNode
        self.tail = startingNode
        self.size = 1

    def addToHead(self, node):
        node.next = self.head
        self.head = node
        self.size += 1

    def addToTail(self, node):
        self.tail.next = node
        self.tail = node
        self.size += 1

    def addToIndex(self, node, index):
        current = self.head
        prev = self.head
        for i in range(0, index):
            prev = current
            current = current.next
        prev.next = node
        node.next = current
        self.size += 1

    def removeHead(self):
        head = self.head
        self.head = self.head.next
        self.size -= 1
        return head

    def removeTail(self):
        tail = self.tail
        current = self.head
        for i in range(0, self.size - 1):
            current = current.next

        self.tail = current
        self.size -= 1
        return tail

    def getHead(self):
        return self.head

    def getTail(self):
        return self.tail

    def printList(self):
        str = ''
        current = self.head
        for i in range(0, self.size):
            str += f'{current.data} -> '
            current = current.next
        print(str)
