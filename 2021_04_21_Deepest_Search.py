from utils.tree_node import Node

test_tree = Node('a', Node('b',Node('d'),Node('e',Node('h'))), Node('c',Node('f',Node('i', Node('k'),Node('l',Node('m'))),Node('j')),Node('g')))

def find_deepest_node(head):
    if head.left is None and head.right is None:
        return (head.val, 0)

    deepest_left, deepest_right = None, None

    if head.left is not None:
        deepest_left = find_deepest_node(head.left)
    
    if head.right is not None:
        deepest_right = find_deepest_node(head.right)

    if deepest_left is None and deepest_right is not None:
        return (deepest_right[0], deepest_right[1] + 1)
    elif deepest_right is None and deepest_left is not None:
        return (deepest_left[0], deepest_left[1] + 1)
    else:
        return (deepest_right[0], deepest_right[1] + 1) if deepest_left[1] < deepest_right[1] else (deepest_left[0], deepest_left[1] + 1)

print(find_deepest_node(test_tree))
