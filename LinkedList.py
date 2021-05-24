from Node import Node

class LinkedList:
    def __init__(self, startingNode = None):
        if startingNode:
            self.head = startingNode
            self.tail = startingNode
            self.size = 1
        self.head = Node()
        self.tail = Node()
        self.size = 0

    def addToHead(self, node):
        node.next = self.head
        self.head = node
        self.size += 1

    def addToTail(self, node):
        if self.tail.data is None:
            current = self.head
            for i in range(0, self.size - 1):
                current = current.next
            current.next = node
            self.tail = node

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

    def getIndex(self, index):
        current = self.head
        for i in range(0, index):
            current = current.next
        return current

    def getList(self):
        str = ''
        current = self.head
        for i in range(0, self.size + 1):
            if i == self.size:
                str += '/'
                return str
            str += f'{current.data} -> '
            current = current.next


    def printList(self):
        str = ''
        current = self.head
        for i in range(0, self.size + 1):
            if i == self.size:
                str += '/'
                print(str)
            str += f'{current.data} -> '
            current = current.next

