class Node:
    def __init__(self, val, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

def find_minimum_path(head) -> int:
    if head.left is None and head.right is None:
        return head.val
    elif head.left is not None and head.right is not None:
        sum_left = find_minimum_path(head.left)
        sum_right = find_minimum_path(head.right)
        return head.val + min(sum_left, sum_right)
    elif head.left is not None:
        sum_left = find_minimum_path(head.left)
        return head.val + sum_left
    else:
        sum_right = find_minimum_path(head.right)
        return head.val + sum_right

    

if __name__ == "__main__":
    test = Node(5, Node(3, Node(-2, Node(-1, Node(-2)), Node(4, Node(-4)))), Node(-1, Node(3), Node(-4)))
    print(find_minimum_path(test));