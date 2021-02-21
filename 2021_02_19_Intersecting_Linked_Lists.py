class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        
def list_length(head):
    temp_head = head
    count = 0
    while temp_head is not None:
        temp_head = temp_head.next
        count += 1

    return count
 
def nth_node(head, n):
    for i in range(n):
        head = head.next
    return head

def find_intersection(lists):
    head_a, head_b = lists[0], lists[1]

    a_length = list_length(head_a)
    b_length = list_length(head_b)

    if a_length > b_length:
        head_a = nth_node(head_a, a_length - b_length)
    elif a_length < b_length:
        head_b = nth_node(head_b, b_length - a_length)
    
    while True:
        if head_a == head_b:
            return head_a
        else:
            head_a, head_b = head_a.next, head_b.next


def construct_test_1():
    intersection = Node(8, Node(10))
    list_a = Node(3, Node(7, intersection))
    list_b = Node(99, Node(1, intersection))
    return (list_a, list_b)

assert find_intersection(construct_test_1()).val == 8

def construct_test_2():
    intersection = Node(8, Node(10))
    list_a = Node(7, intersection)
    list_b = Node(99, Node(1, intersection))
    return (list_a, list_b)

assert find_intersection(construct_test_2()).val == 8

def construct_test_3():
    intersection = Node(8, Node(10))
    list_a = Node(99, Node(1, intersection))
    list_b = Node(7, intersection)
    return (list_a, list_b)

assert find_intersection(construct_test_3()).val == 8

