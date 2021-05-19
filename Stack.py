class Stack:
    def __init__(self):
        self.items = []

    def pop(self):
        item = self.items[0]
        self.items = self.items[1:]
        return item

    def push(self, item):
        addOn = [item]
        self.items[:0] = addOn

    def peak(self):
        print(self.items[0])

    def print(self):
        for i in range(len(self.items)):
            print(i, self.items[i])


