class Node:
	def __init__(self, left=None, right=None, locked=False):
		self.is_locked = locked
		self.parent = None
		
		self.left = left
		if self.left is not None:
			self.left.parent = self 

		self.right = right
		if self.right is not None:
			self.right.parent = self

	def lock(self):
		if not self.is_locked and self.__check_descendants(self) and self.__check_ancestors(self):
			self.is_locked = True
			return True
		else:
			return False
	
	def unlock(self):
		if self.is_locked and self.__check_descendants(self) and self.__check_ancestors(self):
			self.is_locked = False
			return True
		else:
			return False

	def __check_descendants(self, node):
		if node.is_locked and node is not self:
			return False
		elif node.left == None and node.right == None:
			return True
		else:
			return self.__check_descendants(node.left) and self.__check_descendants(node.right)

	def __check_ancestors(self, node):
		if node.is_locked and node is not self:
			return False
		elif node.parent == None:
			return True
		else:
			return self.__check_ancestors(node.parent)


node_7 = Node()
node_6 = Node()
node_5 = Node()
node_4 = Node()
node_3 = Node(node_6, node_7)
node_2 = Node(node_4, node_5)
node_1 = Node(node_2, node_3)

assert node_2.lock()   == True
assert node_3.lock()   == True
assert node_2.unlock() == True
assert node_6.lock()   == False
assert node_3.unlock() == True
assert node_7.lock()   == True
assert node_1.lock()   == False
assert node_4.lock()   == True
assert node_5.lock()   == True
assert node_2.lock()   == False

