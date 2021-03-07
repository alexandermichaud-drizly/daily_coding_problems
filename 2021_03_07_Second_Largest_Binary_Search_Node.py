from utils.tree_node import Node

def get_second_largest(head):
    largest = head
    second_largest = head

    queue = [head]
    while len(queue) > 0:
        node = queue[0]
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
        
        if node.val > largest.val:
            second_largest = largest
            largest = node
        elif node.val > second_largest.val:
            second_largest = node
        queue.pop(0)

    return second_largest

test_tree = Node(3, Node(1, Node(4), Node(9)), Node(2, Node(3, Node(4), Node(6))))

print(get_second_largest(test_tree).val)
