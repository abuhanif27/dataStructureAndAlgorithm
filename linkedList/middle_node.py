from my_linked_list import LinkedList


class InsufficientItem(Exception):
    pass


class MiddleNode(LinkedList):
    def get_middle_node(self):
        if self._is_empty() or self.length == 1:
            raise InsufficientItem("Linked List is In sufficient to get Middle Node")
        mid_index = int(self.length / 2)
        mid_node = self.get(mid_index)
        return mid_node


if __name__ == "__main__":
    ll = MiddleNode()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.append(7)
    print(ll)
    try:
        print("Middle Node is: ", ll.get_middle_node())
    except InsufficientItem as e:
        print(e)
