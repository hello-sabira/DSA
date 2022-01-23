from _queue import Empty  # More efficient and better to use queue based stack


# LIFO Stack implementation using a Python list
class ArrayStack:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def push(self, e):  # Add element to the top of stack
        self.data.append(e)

    def pop(self):      # Notice, no e here
        if self.is_empty():
            raise Empty("Stack is empty")
        else:
            return self.pop()  # Remove last item from list

    def peek(self):  # Sometimes also mentioned as top
        if self.is_empty():
            raise Empty("Stack is empty")
        else:
            return self.data[-1]
