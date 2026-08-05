class Node:
    def __init__(self,key,val, prev, next):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node(0,0,None,None)
        self.tail = Node(0,0,self.head, None)
        self.head.next = self.tail
        self.map = dict()
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.get(key)
            self.map[key].val = value
        else:
            node = Node(key,value,self.tail.prev, self.tail)
            self.map[key] = node
            self.tail.prev.next = node
            self.tail.prev = node
            self.size+=1
        if (self.size > self.capacity):
            node = self.head.next
            self.map.pop(node.key)
            self.size-=1
            self.head.next = self.head.next.next
            self.head.next.prev = self.head
