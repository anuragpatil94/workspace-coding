# HOw to write docstrings
# """
# Summary line.

# Extended description of function.

# Parameters
# ----------
# arg1 : int
#     Description of arg1
# arg2 : str
#     Description of arg2

# Returns
# -------
# int
#     Description of return value

# """
# help(my_function)


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linked_list:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node

    def length(self):
        current = self.head
        count = 0
        while current.next != None:
            count = count + 1
            current = current.next
        return count

    def get(self, index):
        if self.length() == 0:
            return "The Linked List is Empty"
        elif index < 0:
            return "Error: 'Get' Index should be a positive Integer"
        elif (index >= self.length()):
            return "Error: 'Get' Index out of range!"
        current_index = 0
        current_node = self.head
        while True:
            current_node = current_node.next
            if current_index == index:
                return current_node.data
            current_index = current_index + 1

    def erase(self, index):
        if self.length() == 0:
            return "The Linked List is Empty"
        elif index < 0:
            return "Error: 'Get' Index should be a positive Integer"
        elif index >= self.length():
            return "Error: 'Get' Index out of range!"
        current_index = 0
        current_node = self.head
        while True:
            last_node = current_node
            current_node = current_node.next
            if current_index == index:
                last_node.next = current_node.next
                return "Deleted:", current_node.data
            current_index = current_index + 1

    def display(self):
        elems = []
        current = self.head
        while current.next != None:
            current = current.next
            elems.append(current.data)
        print(elems)
