from utils.tree_node import Node

def invert_tree(head) -> Node:
    if head.left is None and head.right is None:
        return Node(head.val)

    new_left = None
    new_right = None
    if head.left is not None:
        new_right = invert_tree(head.left)
    if head.right is not None:
        new_left = invert_tree(head.right)
    
    return Node(head.val, new_left, new_right)

def print_tree(head: Node) -> None:
    print(head.val)

    if head.left is not None:
        print_tree(head.left)
    if head.right is not None:
        print_tree(head.right)

if __name__ == "__main__":
    test = Node('a', Node('b', Node('d'), Node('e')), Node('c', Node('f')))
    result = Node('a', Node('c', Node('f')), Node('b', Node('e'), Node('d')))

    print_tree(invert_tree(test))
    print_tree(result)