# A Library for DoublyLinkedList


class Node:
    '''Node Structure for Doubly Linked List'''
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.previous = None


class DLL:
    def __init__(self):
        self.head = Node()
        self.firstNode = self.head
        self.lastNode = self.head

    def length(self):
        '''This Function finds the length of the Linked List and returns a Value. O(n)'''
        current = self.head
        count = 0
        while current.next != None:
            current = current.next
            count += 1
        return count

    def append(self, data, index=None):
        '''
        This Function adds a Node to the linkedlist either at the end (If index not specified) or at a particular index - O(n)
        Parameters:
        data -- stores any form of data
        index -- The index at which Node to be appended(default None)
        '''
        new_node = Node(data)
        current = self.head
        _index = 0

        if(self.length == 0):
            self.firstNode = new_node
            self.firstNode.previous = self.head
            return
        # O(1) for appending element at last
        if(index == None):
            self.lastNode.next = new_node
            new_node.previous = self.lastNode
            self.lastNode = new_node
            return
        elif (index != None and index > self.length()):
            print("Index cannot be greater the the length of LinkedList")
            return

        while current.next != None:
            if(index != None and index == _index):
                next_node = current.next
                new_node.next = next_node
                current.next = new_node
                new_node.previous = current
                next_node.previous = new_node
                return
            current = current.next
            _index += 1
        # current.next = new_node
        # self.lastNode = new_node
        # new_node.previous = current

    def get(self, index):
        '''Returns a node at particular Index - O(n)'''
        current = self.head
        _index = 0
        while _index != index:
            current = current.next
            _index += 1
        return current

    def delete(self, index):
        '''Deletes a Node with the index'''

    def display(self):
        '''Prints a Linked List Representation - O(n)'''
        current = self.head
        print('Head <--> ', sep=' ', end=' ')
        while current.next != None:
            current = current.next
            print(current.data, ' <--> ', sep=' ', end=' ')
        print(' END ')


# print(l.get(2).previous.data)
# print(l.get(2).next.data)
