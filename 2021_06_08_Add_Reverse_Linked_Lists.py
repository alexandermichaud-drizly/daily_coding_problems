class Node:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next

def add(head1, head2) -> Node:
    carryover = 0
    output_head = None
    output_tail = None
    while head1 is not None or head2 is not None:
        temp_sum = carryover        
        if head1 is None:
            temp_sum += head2.val
            head2 = head2.next 
        elif head2 is None:
            temp_sum += head1.val
            head1 = head1.next 
        else:
            temp_sum += head1.val + head2.val
            head1 = head1.next
            head2 = head2.next
       
        node_val = temp_sum % 10 
        carryover = int((temp_sum - node_val) / 10)

        if output_head is None:
            output_head = Node(node_val)
        elif output_tail is None:
            next_node = Node(node_val)
            output_head.next = next_node
            output_tail = next_node
        else:
            output_tail.next = Node(node_val)
            output_tail = output_tail.next
    return output_head

if __name__ ==  "__main__":
    head1 = Node(1, Node(3, Node(3, Node(1, Node(8)))))
    head2 = Node(6, Node(7, Node(2, Node(4, Node(5, Node(5, Node(3)))))))
    sum_head = add(head1,head2)
    while sum_head is not None:
        print(sum_head.val)
        sum_head = sum_head.next