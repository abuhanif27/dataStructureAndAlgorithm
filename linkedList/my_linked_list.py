class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, value=None):
        self.head = Node(value) if value is not None else None
        self.tail = self.head
        self.length = 1 if value is not None else 0

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        if self.length == 0:
            self.tail = new_node
        self.length += 1

    def append(self, value):
        new_node = Node(value)
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node
        if self.length == 0:
            self.head = new_node
        self.length += 1

    def insert_at(self, position, value):
        if position < 0 or position > self.length:
            raise ValueError('Position must be between 0 and the length of the linked list')
        if position == 0:
            self.prepend(value)
        elif position == self.length:
            self.append(value)
        else:
            new_node = Node(value)
            prev = self.head
            for _ in range(position - 1):
                prev = prev.next
            new_node.next = prev.next
            prev.next = new_node
            self.length += 1

    def pop_end(self):
        if self.length == 0:
            print("The list is already empty")
            return
        if self.length == 1:
            print(f'"{self.head.value}" has been removed successfully')
            self.empty_list()
            return
        current = self.head
        while current.next != self.tail:
            current = current.next
        current.next = None
        print(f'"{self.tail.value}" has been removed successfully')
        self.tail = current
        self.length -= 1

    def pre_pop(self):
        if self.length == 0:
            print("The list is already empty")
            return
        if self.length == 1:
            self.pop_end()
            return
        removed_value = self.head.value
        self.head = self.head.next
        self.length -= 1
        print(f'"{removed_value}" has been removed successfully')

    def pop_at(self, position):
        if position < 0 or position >= self.length:
            raise IndexError("Invalid index")
        if position == 0:
            self.pre_pop()
        elif position == self.length - 1:
            self.pop_end()
        else:
            prev = self.head
            for _ in range(position - 1):
                prev = prev.next
            removed_value = prev.next.value
            prev.next = prev.next.next
            self.length -= 1
            print(f'"{removed_value}" has been removed from index {position}')

    def reverse(self):
        if self.length <= 1:
            return
        prev, current = None, self.head
        self.tail = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        print("Linked list reversed successfully")

    def empty_list(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get_info(self):
        if self.length == 0:
            print("The list is empty")
            return
        print(f"Head: {self.head.value}\nTail: {self.tail.value}\nLength: {self.length}")

    def print_list(self):
        if self.length == 0:
            print("The list is empty")
            return
        current = self.head
        print("Linked List chains are: ", end='')
        while current:
            print(current.value, end=' -> ' if current.next else '')
            current = current.next
        print()


if __name__ == '__main__':
    ll = LinkedList(5)  # List: 5
    ll.append(3)  # List: 5 -> 3
    ll.append(4)  # List: 5 -> 3 -> 4
    ll.prepend(1)  # List: 1 -> 5 -> 3 -> 4
    ll.prepend(10)  # List: 10 -> 1 -> 5 -> 3 -> 4

    # Insert value 2 at position 1
    try:
        ll.insert_at(1, 2)  # List: 10 -> 2 -> 1 -> 5 -> 3 -> 4
    except ValueError as e:
        print(e)

    ll.pop_end()  # Removes 4, List: 10 -> 2 -> 1 -> 5 -> 3
    ll.pre_pop()  # Removes 10, List: 2 -> 1 -> 5 -> 3
    ll.pop_at(2)  # Removes value at index 2 (5), List: 2 -> 1 -> 3

    ll.print_list()  # Output: 2 -> 1 -> 3
    ll.get_info()  # Output: Head: 2, Tail: 3, Length: 3

    ll.reverse()  # Reverses the list: 3 -> 1 -> 2
    ll.print_list()  # Output: 3 -> 1 -> 2
    ll.get_info()  # Output: Head: 3, Tail: 2, Length: 3
