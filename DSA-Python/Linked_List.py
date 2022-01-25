# Linked lists are better than arrays in terms of memeory managmenet and insertion is also easier

class Node:   # this class will represent an individual element in the linked list
    def __init__(self, data=None, next=None):
        self.data = data  # one class member is called data, which of course, contains data
        self.next = next  # next, which points to the next element


class LinkedList:
    def __init__(self):
        self.head = None  # by head, we mean the head value we are pointing to in the linked list

    def print(self):
        if self.head is None:   # of course if head is empty, it means there's no body and hence linked list is also empty
            print("Linked list is empty")
            return
        itr = self.head  # just a temp iterating variable, currently my head, later we will move to next using it
        result = ''  # a string to append our result
        while itr:  # aka while itr has a head
            result += str(itr.data)+' --> ' if itr.next else str(itr.data)  # increment our result string with the data within the itr
            itr = itr.next  # now we change itr val to the next node's val
        print(result)

    def get_length(self):  # just iterate, count, append and that's your length!
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    def insert_at_beginning(self, data):
        node = Node(data, self.head)  # creating a node element
        self.head = node  # since we're inserting at the beginning my head will be the node i just created rn, REMEMBER! HEAD IS THE ELEMENT FROM WHICH A --> EMERGES, NOT THE ELEMENT THE ARROW IS POINTING TO! THAT'S THE TAIL

    def insert_at_end(self, data):
        if self.head is None:  # aka if you're the very first element of the linked list
            self.head = Node(data, None)  # then the tail emerging from you is null
            return

        itr = self.head  # another temp iterating variable
        while itr.next:  # now as long as it has a next element, aka it's pointing to something,
            itr = itr.next  # bloody keep iterating! as we need to go to the end of the last arrow to insert ourself

        itr.next = Node(data, None)  # when you reach this point it means all iterating is done, you're at the end of the tunnel, now put yourself and the element you'll be pointing to is null!

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():  # of course check the index so it's within range
            raise Exception("Invalid Index")

        if index == 0:  # if index is zero, let's make use of the insert at beginning function to insert data
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head  # otherwise, again initialize itr to zero
        while itr:  # while itr has some value
            if count == index - 1:  # check if position of count is at the element right before where we want to enter the new element
                node = Node(data, itr.next)  # creating a new node with data and the pointer pointing to next element
                itr.next = node  # itr.next is equal to node // aka here the itr.next is where count == index
                break  # once you're done, break out!

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():  # of course check the index so it's within range
            raise Exception("Invalid Index")

        if index == 0:  # so we are trying to remove the head, the very first val from which a tail/arrow emerges
            self.head = self.head.next  # we can not survive headless, hence set head to the next val which emerged from the soon to be removed curRent head
            return

        count = 0   # important concept here:
        itr = self.head  # say the temporary itr variable is initially equal to head
        while itr:  # while itr has some val
            if count == index - 1:  # this if statement tells us if count is == index-1, aka, the count is at the position right before the element we're trying to remove
                itr.next = itr.next.next  # then set itr.next = itr.next.next aka we're breaking the link b/w current element and next element and making this current element point to the next to next element
                break # and then break as we're done with our job

            itr = itr.next
            count += 1

    def insert_values(self, data_list):  # to make a new linked list from a list
        self.head = None
        for data in data_list:
            self.insert_at_end(data)  # using insert at end here so that first  val of data list remains as head


if __name__ == '__main__':
    ll = LinkedList()
    print("inserting at end, we expect 79 (bcoz no tail emerging from us, then 79-->1 then finally 79-->1-->9876")
    ll.insert_at_end(79)
    ll.print()
    ll.insert_at_end(1)
    ll.print()
    ll.insert_at_end(9876)
    ll.print()
    rr = LinkedList()
    print("inserting at beginning, we expect 79, then 1--> 79 as we just changed head to 1 (from which a tail will appear), then finally 9876-->1->79")
    rr.insert_at_beginning(79)
    rr.print()
    rr.insert_at_beginning(1)
    rr.print()
    rr.insert_at_beginning(9876)
    rr.print()
    ss = LinkedList()
    ss.insert_values(["banana", "mango", "grapes", "orange"])