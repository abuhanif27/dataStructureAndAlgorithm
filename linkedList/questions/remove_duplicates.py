from linkedList.my_linked_list import LinkedList


class RemoveDuplicates(LinkedList):
    def remove_duplicates(self):
        values = set()
        previous = None
        current = self.head
        while current:
            if current.value not in values:
                values.add(current.value)
                previous = current
            else:
                previous.next = current.next
                self.length -= 1
            current = current.next


if __name__ == '__main__':
    linked_list = RemoveDuplicates()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.append(4)
    linked_list.append(5)
    print(linked_list)
    linked_list.remove_duplicates()
    print(linked_list)
