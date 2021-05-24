from LinkedList import *
from Queue import Queue
from math import inf

class Graph:
    def __init__(self):
        self.adjList = []
        self.numNodes = 0

    def addNode(self, node):
        self.adjList.append(node)
        self.adjList[node.data] = LinkedList()
        self.numNodes += 1

    def addEdge(self, source, dest):
        self.adjList[source].addToHead(Node(dest))
        self.adjList[dest].addToHead(Node(source))

    def printAdjacency(self):
        for i in range(len(self.adjList)):
            print(f'{i} : {self.adjList[i].getList()}')

    def bfs(self, source, dest):
        queue = Queue()
        visited = [False] * self.numNodes
        parent = [-inf] * self.numNodes
        visited[source] = True
        queue.enque(source)

        while not queue.getSize() == 0:
            vertex = queue.deque()
            if vertex.data == dest:
                print(f'Destination: {dest} found!')
                return

            if not vertex.data == dest:
                current = self.adjList[vertex.data].getHead()
                for i in range(self.adjList[vertex.data].getSize()):
                    if not visited[current.data]:
                        visited[current.data] = True
                        queue.enque(current.data)
                        parent[current.data] = vertex.data
                    current = current.next
        print(f'Destination: {dest} not found.')


