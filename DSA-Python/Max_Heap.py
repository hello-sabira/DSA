# Full, complete Binary Tree with lower layer incomplete, (little full from left to right)
# Every parent node > its children in Max heap, reverse for Min heap
# When we insert, we must always go from down to up (as left as possible) , to follow binary tree properties
# During deletion, go from top to down
# Insert -> O (log n)
# Get max in O(1)
# Remove max in O(log n)

class MaxHeap:
    def __init__(self, items=[]):
        super().__init__()
        self.heap = [0]  # index zero
        for i in items:
            self.heap.append(i)
            self.__floatUp(len(self.heap) - 1)

# Max heap operations: 1. push, 2. peek, 3. getMax

    # add val to end of the array, and float it up to proper position
    def push(self, data):  # aka insert element
        self.heap.append(data)  # append to list
        self.__floatUp(len(self.heap) - 1)  # then float it up to proper position

    def peek(self):  # aka get max, aka the top one as it's max heap
        if self.heap[1]:  # if we have at least 1 val in heap
            return self.heap[1]  # return the top one
        else:
            return False  # else false, of course

    # move max to end of array -> delete it -> bubble down the item at index 1 to its proper position -> return max
    def pop(self):  # aka delete element
        if len(self.heap) > 2:  # scenario 1: we have more than 2 elements in heap, so:
            self.__swap(1, len(self.heap) - 1)  # rule is to always delete element at node 1
            max = self.heap.pop()
            self.__bubbleDown(1)
        elif len(self.heap) == 2:  # scenario 2: only 1 val in heap
            max = self.heap.pop()
        else:  # scenario 3: heap is empty
            max = False
        return max

# all the functions below are private internal functions

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __floatUp(self, index):
        parent = index // 2  # formula to find ever child node's parent
        if index <= 1:  # if we're at top, nothing to do
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__floatUp(parent) # recursively calling floatup to swap positions until proper position when if statement is false

    def __bubbleDown(self, index): # also known as max heapify
        left = index * 2  # formula for left child position
        right = index * 2 + 1  # formula for right child position
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.__swap(index, largest)
            self.__bubbleDown(largest)


m = MaxHeap([95, 3, 21])
m.push(10)
print(str(m.heap[0:len(m.heap)]))
print(str(m.pop()))
