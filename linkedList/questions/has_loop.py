from linkedList.questions.middle_node import MiddleNode


class HasLoop(MiddleNode):
    def has_loop(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True  # Cycle detected
        return False  # No cycle detected


if __name__ == '__main__':
    ll = HasLoop()
    ll.append(1)
    ll.append(2)
    ll.append(3)

    # To test cycle detection, uncomment the following line
    # ll.head.next.next.next = ll.head  # Create a cycle for testing

    print(ll.has_loop())  # Should print True if cycle is created, False otherwise
