from LinkedList import *
class Graph:
    def __init__(self):
        self.adjList = []

    def addNode(self, node):
        self.adjList.append(node)
        self.adjList[node.data] = LinkedList()

    def addEdge(self, source, dest):
        self.adjList[source].addToHead(Node(dest))
        self.adjList[dest].addToHead(Node(source))

    def printAdjacency(self):
        for i in range(len(self.adjList)):
            print(f'{i} : {self.adjList[i].getList()}')
