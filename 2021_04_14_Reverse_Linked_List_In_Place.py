from utils.node import Node

def reverse_list(head):
    prev = head
    head = head.next
    prev.next = None
    temp = ''

    while temp is not None:
        temp = head.next
        head.next = prev
        prev = head
        if temp is not None:
            head = temp

    return head

if __name__ == "__main__":
    test = Node(4,Node(3,Node(2,Node(1))))
    list_reversed = reverse_list(test)
    while list_reversed is not None:
        print(list_reversed.val)
        list_reversed = list_reversed.next
