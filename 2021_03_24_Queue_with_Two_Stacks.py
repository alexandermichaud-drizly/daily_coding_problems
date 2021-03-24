class Queue:
		def __init__(self):
					self.main_stack = []			
					self.helper_stack = []

		def enqueue(self, n):
					while len(self.main_stack) > 0:
							self.helper_stack.append(self.main_stack.pop())

					self.main_stack.append(n)

					while len(self.helper_stack) > 0:
							self.main_stack.append(self.helper_stack.pop())

		def dequeue(self):
				return self.main_stack.pop()

if __name__ == "__main__":
		queue = Queue()
		queue.enqueue(1)
		queue.enqueue(2)
		queue.enqueue(3)
		print(queue.dequeue())
		queue.enqueue(4)
		print(queue.dequeue())
		print(queue.dequeue())
		print(queue.dequeue())

