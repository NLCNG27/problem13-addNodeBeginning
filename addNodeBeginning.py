# Author: Nguyen L.
# Date: May 30th, 2020
# Add a node at the beginning of the linked list

from random import randint

# Node class
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# LinkedList class
class LinkedList:
    def __init__(self, data=None):
        self.head = Node(data)

    # insert beginning method
    def addBeginning(self, newData):
        temp = Node(newData)
        temp.next = self.head
        self.head = temp

    # generating random list of nodes
    def randomList(self, limit=5):
        i = 0

        while i < limit:
            value = randint(1, 20)
            self.addBeginning(value)
            i += 1

        self.display()


    # display method
    def display(self):
        temp = self.head

        while temp.next != None:
            print(temp.data, end=" ")
            temp = temp.next    


# TESTING OUT THE PROGRAM
myList = LinkedList()
limit = randint(5, 10)
print("*" * 40)
print("Original list: ", end="")
myList.randomList(limit)
print()

value = int(input("Enter your value to add at beginning of list: "))
myList.addBeginning(value)
print("New list: ", end="")
myList.display()
print()


