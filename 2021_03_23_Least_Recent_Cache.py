class DoubleLinkedNode:
		def __init__(self, val, prev=None, next=None):
				self.val  = val
				self.prev = prev
				self.next = next

class Cache:
		def __init__(self,n):
				self.capacity = n
				self.items = 0
				self.hash = {}
				self.list_head = None
				self.list_tail = None

		def set_key(self,key,val):
				node = DoubleLinkedNode(val)
				self.hash[key] = node
				
				if self.list_head is None:
						self.list_head, self.list_tail = node, node 
						self.items = 1
				else:
						self.list_head.prev = node
						self.list_head = node

						if self.items < self.capacity:
								self.items += 1
						else:
								self.list_tail = self.list_tail.prev

		def get(self,key):
				if key not in self.hash:
						return None
				
				node = self.hash[key]
				if node is self.list_head:
						pass
				else:
						if node is self.list_tail:
								node.prev.next = None 
						else:
								node.next.prev = node.prev
								node.prev.next = node.next
						
						node.prev = None
						node.next = self.list_head
						self.list_head = node.next
				return node.val


# driver code

if __name__ == "__main__":
		cache = Cache(3)
		cache.set_key('a','foo')
		print("Head: " + cache.list_head.val + "; Tail: " + cache.list_tail.val) 
		cache.set_key('b','bar')
		print("Head: " + cache.list_head.val + "; Tail: " + cache.list_tail.val) 
		cache.set_key('c','fizz')
		print("Head: " + cache.list_head.val + "; Tail: " + cache.list_tail.val) 
		print("C: " + cache.get('c'))
		print("Head: " + cache.list_head.val + "; Tail: " + cache.list_tail.val) 
		cache.set_key('d','buzz')
		print("Head: " + cache.list_head.val + "; Tail: " + cache.list_tail.val) 
		print("D: " + cache.get('d'))
		print("Head: " + cache.list_head.val + "; Tail: " + cache.list_tail.val) 

