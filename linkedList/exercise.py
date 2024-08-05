class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def _initialize_list(self, value):
        """Initializes the linked list with a single node."""
        new_node = Node(value)
        self.head = self.tail = new_node
        self.length = 1

    def _is_empty(self):
        """Checks if the linked list is empty."""
        return self.length == 0

    def prepend(self, value):
        """Adds a node with the given value to the beginning of the list."""
        if self._is_empty():
            self._initialize_list(value)
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
            self.length += 1

    def append(self, value):
        """Adds a node with the given value to the end of the list."""
        if self._is_empty():
            self._initialize_list(value)
        else:
            new_node = Node(value)
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    def insert(self, index, value):
        """Inserts a node with the given value at the specified index."""
        if index < 0 or index > self.length:
            raise IndexError('Index out of range')
        if index == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        else:
            new_node = Node(value)
            current_node = self.head
            for _ in range(index - 1):
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node
            self.length += 1

    def pop_first(self):
        """Removes the first node of the list."""
        if self._is_empty():
            raise IndexError('List is empty')
        if self.length == 1:
            self._clear_list()
        else:
            self.head = self.head.next
            self.length -= 1

    def pop(self):
        """Removes the last node of the list."""
        if self._is_empty():
            raise IndexError('pop from empty linked list')
        if self.length == 1:
            self._clear_list()
        else:
            current_node = self.head
            for _ in range(self.length - 2):
                current_node = current_node.next
            current_node.next = None
            self.tail = current_node
            self.length -= 1

    def remove(self, index):
        """Removes the node at the specified index."""
        if index < 0 or index >= self.length:
            raise IndexError('Index out of range')
        if self._is_empty():
            raise IndexError('List is empty')
        if index == 0:
            self.pop_first()
        else:
            current_node = self.head
            for _ in range(index - 1):
                current_node = current_node.next
            current_node.next = current_node.next.next
            if index == self.length - 1:
                self.tail = current_node
            self.length -= 1

    def get(self, index):
        """Retrieves the node at the specified index."""
        if index < 0 or index >= self.length:
            raise IndexError('List index out of range')
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        return current_node

    def set_value(self, index, value):
        """Sets the value of the node at the specified index."""
        target_node = self.get(index)
        if target_node:
            target_node.value = value

    def reverse(self):
        """Reverses the linked list in place."""
        if self.length <= 1:
            return
        current_node = self.head
        previous_node = None
        self.tail = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        self.head = previous_node

    def _clear_list(self):
        """Clears the linked list."""
        self.head = self.tail = None
        self.length = 0

    def __repr__(self):
        """Represents the linked list as a string."""
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return f"""
        head = {self.head}
        tail = {self.tail}
        length = {self.length}
        =======================
        linked list items:
        {' -> '.join(values)}
        """


if __name__ == '__main__':
    # Creating a linked list instance and performing various operations
    ll = LinkedList()
    ll.append(2)          # Appending 2 to the list
    ll.append(3)          # Appending 3 to the list
    ll.prepend(0)         # Prepending 0 to the list
    ll.prepend(3)         # Prepending 3 to the list
    ll.prepend(6)         # Prepending 6 to the list
    ll.prepend(5)         # Prepending 5 to the list
    ll.pop()              # Popping the last element
    ll.pop_first()        # Popping the first element
    ll.set_value(2, 4)    # Setting the value of the node at index 2 to 4
    print(ll)             # Printing the current state of the linked list
    ll.insert(1, 5)       # Inserting 5 at index 1
    print(ll)             # Printing the current state of the linked list
    ll.remove(2)          # Removing the node at index 2
    print(ll)             # Printing the current state of the linked list
    ll.reverse()          # Reversing the linked list
    print(ll)             # Printing the current state of the linked list
    print(ll.get(2))      # Getting the node at index 2
