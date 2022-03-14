class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if self.is_empty():
            return "is empty"
        else:
            self.items.pop()

    def size(self):
        return len(self.items)

    def first(self):
        if self.is_empty():
            return "is empty"
        else:
            return self.items[-1]

    def print(self):
        for item in self.items:
            print(item )


q = Queue()
q.enqueue(7)
q.enqueue(9)
print(q.first())
q.print()
