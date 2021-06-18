from utils.tree_node import Node

def print_by_level(head) -> None:
    queue = [head]
    while len(queue) > 0:
        front = queue[0]
        if front.left is not None:
            queue.append(front.left)
        if front.right is not None:
            queue.append(front.right)
        print(front.val)
        queue.pop(0)


if __name__ == "__main__":
    test = Node(1, Node(2, Node(4, Node(8), Node(9)), Node(5, Node(10), Node(11))), Node(3, Node(6, Node(12), Node(13)), Node(7, Node(14), Node(15))))
    print_by_level(test)