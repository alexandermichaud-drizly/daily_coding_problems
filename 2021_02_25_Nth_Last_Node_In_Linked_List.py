from utils.node import Node 

def get_nth_from_last(linked_list, n):
    output = linked_list
    for _ in range(n):
        linked_list = linked_list.next

    while linked_list.next is not None:
        output = output.next
        linked_list = linked_list.next

    return output.val
        

test_list = Node(0, Node(1, Node(2, Node(3, Node(4, Node(5))))))
assert get_nth_from_last(test_list, 2) == 3
assert get_nth_from_last(test_list, 3) == 2
assert get_nth_from_last(test_list, 5) == 0

