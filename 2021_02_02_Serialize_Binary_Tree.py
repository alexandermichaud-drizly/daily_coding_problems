class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(node):
    queue = [node]
    output = ''
    while queue:
        if queue[0].left:
            queue.append(queue[0].left)

        if queue[0].right:
            queue.append(queue[0].right)

        output = output + queue[0].val
        queue.pop(0)

    return output
            


def deserialize(node):
    return


test_node = Node('root', Node('left', Node('left.left')), Node('right'))
print serialize(test_node)
# assert deserialize(serialize(test_node)).left.left.val == 'left.left'
