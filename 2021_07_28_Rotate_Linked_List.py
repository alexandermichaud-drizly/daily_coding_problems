from utils.node import Node

def rotate_list(head: Node, k: int) -> Node:
    new_tail = head
    while k > 2:
        new_tail = new_tail.next
        k -= 1
    
    new_head = new_tail.next
    new_tail.next = None
    tail = new_head
    while tail.next is not None:
        tail = tail.next
    
    tail.next = head
    return new_head

if __name__ == "__main__":
    test: Node = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    rotated_list: Node = rotate_list(test, 3) 
    rotated_list.print_linked_list()