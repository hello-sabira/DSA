# FIFO Queue implementation in python using list
from queue import Empty


class ArrayQueue:
    DEFAULT_CAPACITY = 10  # moderate capacity for all new queues

    def __init__(self):
        self.data = [] * ArrayQueue.DEFAULT_CAPACITY  # Creating an empty queue
        self.size = 0
        self.front = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0  # boolean condition

    def first(self):  # Return but don't remove element at front of queue
        if self.is_empty():
            raise Empty('Queue is empty, you fools! :-P')
        return self.data[self.front]

    def dequeue(self):  # Return AND REMOVE! the first element of queue, aka it's FIFO time
        if self.is_empty():
            raise Empty('Queue is empty, you fools! :-P')
        result = self.data[self.front]  # First element
        self.data[self.front] = None  # Gotta help the garbage collection (Y)
        self.front = (self.front + 1) % len(self.data)
        self.size -= 1
        return result

    def enqueue(self):  # Add element to back of queue
        if self.size == len(self.data):  # This is why list based bad, issues with memory
            self.resize(2 * len(self.data))  # Doubling array size
        result = self.data[self.front]  # First element
        available = (self.front + self.size) % len(self.data)
        self.size += 1
        return result

    def resize(self, cap):                 # we assume cap >= len(self) so we resize to a new list of cap >- len(self)
        old = self.data                    # keeping track of our existing list
        self.data = [None] * cap           # allocate list with new capacity
        walk = self.front
        for i in range(self.size):         # only considering existing elements
            self.data[i] = old[walk]       # intentionally shift indices
            walk = (1 + walk) % len(old)   # use old size as modulus
        self.front = 0                     # front has been realigned
