class Node:
    def __init__(self, val, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right

def find_univals(head):
    count = 0
    if (head.left == None and head.right == None):
        return 1
    
    if (head.left is not None):
        count += find_univals(head.left)
    if (head.right is not  None):
        count += find_univals(head.right)

    if (head.left == head.right):
        return 1 + count
    else:
      return count


test_node_1 = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))

print(find_univals(test_node_1))
