class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.mp = {} # store node with key and value
        self.capacity = capacity
        
    def initialize_linked_list(self, key, value):
        self.head = ListNode(key, value)
        self.tail = self.head
        
    def append_node(self, key, value):
        if hasattr(self, 'tail') and self.tail:
            new_node = ListNode(key, value)
            new_node.prev = self.tail
            new_node.next = None
            self.tail.next = new_node
            self.tail = self.tail.next
        else:
            self.initialize_linked_list(key, value)
    
    def remove_node(self, node_to_change):
        if node_to_change is not self.head and node_to_change is not self.tail:
            node_to_change.prev.next = node_to_change.next
            node_to_change.next.prev = node_to_change.prev
            return
        if node_to_change is self.head:
            self.head = self.head.next
        if node_to_change is self.tail:
            self.tail = self.tail.prev
        
    def get(self, key: int) -> int:
        if key in self.mp:
            node_to_move = self.mp[key]
            self.append_node(node_to_move.key, node_to_move.value)
            self.remove_node(node_to_move)
            self.mp[key] = self.tail
            return self.mp[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        self.append_node(key, value)
        if key in self.mp:
            ans = self.mp[key]
            self.remove_node(ans)
            self.mp[key] = self.tail
        else:
            self.mp[key] = self.tail
            if len(self.mp) > self.capacity:
                del self.mp[self.head.key]
                self.head = self.head.next


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)