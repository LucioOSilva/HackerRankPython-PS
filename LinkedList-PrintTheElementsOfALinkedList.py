"""
If you're new to linked lists, this is a great exercise for learning about them. Given a pointer to the head node of a
linked list, print its elements in order, one element per line. If the head pointer is null (indicating the list is
empty), don’t print anything.

Input Format:
The first line of input contains "n", the number of elements in the linked list.
The next "n" lines contain one element each, which are the elements of the linked list.

Note: Do not read any input from stdin/console. Complete the printLinkedList function in the editor below.

Constraints:
1 <= n <= 1000
1 <= list[i] <= 1000, where list[i] is the i[th] element of the linked list.

Output Format:
Print the integer data for each element of the linked list to stdout/console (e.g.: using printf, cout, etc.).
There should be one element per line.

Sample Input:
2
16
13

Sample Output:
16
13

Explanation:
There are two elements in the linked list. They are represented as 16 -> 13 -> NULL. So, the printLinkedList function
should print 16 and 13 each in a new line.
"""


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


def printLinkedList(head):
    cur = llist.head
    while cur.next != None:
        print(cur.data)
        cur = cur.next
    print(cur.data)


if __name__ == '__main__':
    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    printLinkedList(llist.head)
