class Node:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def run(node):
		if isinstance(node.val, int):
				return node.val 
		
		if node.val == "+":
				return run(node.left) + run(node.right)
		elif node.val == "-":
				return run(node.left) - run(node.right)
		elif node.val == "/":
				return run(node.left) / run(node.right)
		elif node.val == "*":
				return run(node.left) * run(node.right)
		else:	
				print("Not valid operation")

test = Node('*', Node('+', Node(3), Node(2)), Node('+', Node(4), Node(5)))

print(run(test))
