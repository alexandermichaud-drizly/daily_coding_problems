from utils.tree_node import Node

def prune(t):
    if t.left is None and t.right is None:
        return None if t.val == 0 else t
    
    return Node(t.val, prune(t.left), prune(t.right))

if __name__ == "__main__":
    test = Node(0, Node(1), Node(0, Node(1, Node(0), Node(0)), Node(0)))
    results = prune(test)

    queue = [results]
    while len(queue) > 0:
        head = queue[0]
        if head.left is not None:
            queue.append(head.left)
        if head.right is not None:
            queue.append(head.right)
        print(head.val)
        queue.pop(0)
