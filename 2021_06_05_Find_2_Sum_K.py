from utils.tree_node import Node

def find_k_sum(head, k, memo={}):
    if (k - head.val) in memo:
        return (head.val, k - head.val)
    memo[head.val] = True
    if head.left is not None and head.right is not None:
        return find_k_sum(head.left, k, memo) or find_k_sum(head.right, k, memo)
    elif head.left is not None:
        return find_k_sum(head.left, k, memo)
    elif head.right is not None:
        return find_k_sum(head.right, k, memo)
    else:
        return None

if __name__ == "__main__":
    test = Node(8, Node(3, Node(12, Node(2), Node(7))), Node(14, Node(1, Node(5), Node(11)), Node(15)))
    print(find_k_sum(test, 21))
