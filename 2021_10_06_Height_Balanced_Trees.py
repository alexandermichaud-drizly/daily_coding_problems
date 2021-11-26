from utils.tree_node import Node

def is_height_balanced_tree(head: Node) -> bool:
  return

unbalanced_tree = Node(0, Node(1, Node(3, Node(7, Node(8))), Node(4)), Node(2, Node(5), Node(6)))
balanced_tree = Node(0, Node(1, Node(3), Node(4, Node(7))), Node(2, Node(5), Node(6)))

if __name__ == "__main__":
    assert is_height_balanced_tree(balanced_tree)
    assert not is_height_balanced_tree(unbalanced_tree)