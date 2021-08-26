# https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list/problem

# hint - if you print(head) it returns an object.
# if you print head.data it returns a value.

# note in the class definition, you have self.next
# if you print head.next you get another object.
# accessing head.next.data gives you yet another value.

# hint, the first line contains "n" the number of elements.
# we get the value, "16" for the first round.

# hint- a recursive function is a function that calls itself.

#     if head is not None:
#        print(head.data)
#        printLinkedList(head.next)

# in the above implementation, in python, the line, "print(head.data)" can't finish
# until all other functions finish. All other functions may never finish after 1000 rounds.
# thus, you go past the recursion depth limit for Python3 which is 1000.

# hence, it is important to use a while loop to close out the successive functions.
# def print_list(node):
#    while head:
#        print(head.data)
#        head = head.next

#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

# Complete the printLinkedList function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def printLinkedList(head):

    while head:
        print(head.data)
        head = head.next

if __name__ == '__main__':
