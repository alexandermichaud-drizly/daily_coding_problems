preorder = ['a','b','d','e','c','f','g']
inorder  = ['d','b','e','a','f','c','g']

class Node:
		def __init__(self, val, left=None, right=None):
				self.val = val
				self.left = left
				self.right = right

class Tree:
		def __init__(self, preorder, inorder):
				self.preorder = preorder
				self.inorder = inorder
				self.__head = None
	
		def build_helper(self):
				if self.preorder[0] == self.inorder[0]:
						node = Node(self.preorder[0])
						del self.preorder[0]
						del self.inorder[0]
						return node

				node = Node(self.preorder[0])
				
				node.left = self.build_helper()
				if node.val == self.inorder[0]:
						del self.inorder[0]

				node.right = self.build_helper()
				if node.val == self.inorder[0]:
						del self.inorder[0]
				
				return node

		def build(self):
				self.__head = self.build_helper()

		def show(self):
				queue = [self.__head]
				j = 0
				k = 0
				while len(queue) > 0:
						front = queue[0]

						if front.left is not None:
								queue.append(front.left)
						if front.right is not None:
								queue.append(front.right)
						if j == 2**k:
								print("\n")
								k += 1
						print(front.val + " ")
						j += 1
						queue.pop(0)

tree = Tree(preorder, inorder)
tree.build()
tree.show()
