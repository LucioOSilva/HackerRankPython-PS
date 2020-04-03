"""
You are given the pointer to the head node of a linked list and an integer to add to the list. Create a new node with
the given integer. Insert this node at the tail of the linked list and return the head node of the linked list formed
after inserting this new node. The given head pointer may be null, meaning that the initial list is empty.

Input Format:
You have to complete the SinglyLinkedListNode Insert(SinglyLinkedListNode head, int data) method which takes two
arguments - the head of the linked list and the integer to insert. You should NOT read any input from stdin/console.

The input is handled by code in the editor and is as follows:

The first line contains an integer n, denoting the number of elements to be inserted at the head of the list.
The next n lines contain an integer each, denoting the element to be inserted.

Constraints:
1 <= n <= 1000
1 <= list[1] <= 1000

Output Format:
Insert the new node at the head and return the head of the updated linked list. Do NOT print anything to stdout/console.
The output is handled by code in the editor and is as follows:
Print the elements of the linked list from head to tail, each in a new line.

Sample Input:
5
383
484
392
975
321

Sample Output:
321
975
392
484
383

Explanation:
Intially the list in NULL. After inserting 383, the list is 383 -> NULL.
After inserting 484, the list is 484 -> 383 -> NULL.
After inserting 392, the list is 392 -> 484 -> 383 -> NULL.
After inserting 975, the list is 975 -> 392 -> 484 -> 383 -> NULL.
After inserting 321, the list is 321 -> 975 -> 392 -> 484 -> 383 -> NULL.
"""

# !/bin/python3

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


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


def insertNodeAtHead(llist, data):
    if llist is None:
        llist = SinglyLinkedListNode(data)
        return llist
    else:
        nnode = SinglyLinkedListNode(data)
        nnode.next = llist
        return nnode


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtHead(llist.head, llist_item)
        llist.head = llist_head

    print_singly_linked_list(llist.head, '\n', fptr)
    fptr.write('\n')

    fptr.close()
