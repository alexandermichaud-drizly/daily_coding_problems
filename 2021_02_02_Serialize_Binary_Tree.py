class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(node):
    queue = [node]
    output = ''
    while queue:
        if queue[0] is not None:
            queue.append(queue[0].left)
            queue.append(queue[0].right)
            output = output + '-' + queue[0].val
        else:
            output = output + '-' +'None'
        queue.pop(0)

    return output
            
def nest(node_list, i=1):
    if i >= len(node_list) or node_list[i] == 'None':
        return None
    else:
        left = nest(node_list, (2*i))
        right = nest(node_list, ((2*i) + 1))
        return Node(node_list[i], left, right)

def deserialize(serialized):
    serialized_list = serialized.split('-')

    return nest(serialized_list)

test_node = Node('root', Node('left', Node('left.left', None, Node('left.left.right'))), Node('right', Node('right.left')))
print(serialize(test_node))
assert deserialize(serialize(test_node)).left.left.right.val == 'left.left.right'
