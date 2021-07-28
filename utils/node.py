class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def print_linked_list(self):
        current = self
        while current is not None:
            print(current.val)
            current = current.next