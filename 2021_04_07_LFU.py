class Node:
    def __init__(self,n,prev=None,next=None):
        self.frequency = n
        self.dict = {}
        self.prev = prev
        self.next = next

    def add(self,k,v):
        self.dict[k] = v

    def remove_first(self):
        key = next(iter(self.dict))
        del self.dict[key]
        return key

    def remove(self,k):
        return self.dict.pop(k,None)

    def is_empty(self):
        return not self.dict


class LFU:
    def __init__(self,n):
        self.vacancy = n
        self.dict = {}
        self.least = Node(0)

    def set(self,k,v):
        if self.vacancy == 0:
            self.least.remove_first()
            if self.least.is_empty():
                self.least = self.least.next
        else:
            self.vacancy -= 1

        if self.least.frequency > 0:
            new_node = Node(0, next=self.least)
            self.least = new_node

        self.dict[k] = self.least
        self.least.add(k,v)

    def get(self,k):
        node = self.dict[k]
        v = node.remove(k)
        if node.next is None:
            node.next = Node(node.frequency + 1,prev=node)
        node.next.add(k,v)

        if node.is_empty():
            if node.prev is not None:
                node.prev.next = node.next
            else:
                self.least = node.next
            node.next.prev = node.prev
            
        print(v)

if __name__ == "__main__":
    cache = LFU(3)
    cache.set(1, 'first')
    cache.set(2, 'second')
    cache.set(3, 'third')
    cache.get(1)
    cache.get(2)
    cache.set(4, 'fourth')
    cache.get(4)
    cache.get(3)


