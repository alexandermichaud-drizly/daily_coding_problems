from utils.node import Node

def swap_every_two(head) -> Node:
    first = head
    second = head.next
    while second is not None:
        temp = second.val
        second.val = first.val
        first.val = temp

        if second.next is not None:
            first = second.next
            second = first.next
        else:
            first, second = None, None

    return head



if __name__ == "__main__":
    test = Node(1,Node(2,Node(3,Node(4))))
    result = swap_every_two(test)
    while result is not None:
        print(result.val)
        result = result.next

    test = Node(1,Node(2,Node(3)))
    result = swap_every_two(test)
    while result is not None:
        print(result.val)
        result = result.next