class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None
    def insert(self,data):
        node= Node(data)
        node.next = self.head
        self.head = node
    def traver(self):
        current = self.head
        while current != None:
            print(current.data, end ='->')
            current = current.next
    def swap_head_tail(self):
        if self.head is None or self.head.next is None:
            return  # list is empty or has only one node

        old_head = self.head
        old_tail = self.head
        while old_tail.next is not None:
            old_tail = old_tail.next

        # Swap head and tail
        self.head = old_tail
        old_tail.next = old_head
        old_head.next = None
    def insert_on_start(self, node):
        new_node = Node(node)
        current_head = self.head
        self.head = new_node
        new_node.next = current_head
    def insert_on_tail(self, node):
        n = Node(node)
        current = self.head
        while current.next:
            current = current.next
        current.next = n

        
list = linkedlist()

list.insert(10)
list.insert(100)
list.insert(1000)
# list.swap_head_tail()
# list.insert_on_start(15)
list.insert_on_tail(105)
list.traver()