class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def insert_at_start(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node

    def delete_at_start(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            self.head = self.head.next

    def insert_at_index(self, index, data):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            counter = 0
            temp = self.head
            while counter < index - 1 and temp.next:
                temp = temp.next
                counter += 1
            new_node.next = temp.next
            temp.next = new_node

    def delete_at_index(self, index):
        temp = self.head
        if index == 0:
            if self.head is None:
                print("Linked list is empty")
                return
            self.head = self.head.next
            return
        prev = None
        counter = 0
        while temp is not None and counter < index:
            prev = temp
            temp = temp.next
            counter += 1
        if temp is None:
            print(f"Index {index} out of bounds")
            return
        prev.next = temp.next

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def delete_at_end(self):
        if self.head is None:
            print("Linked List is empty")
        elif self.head.next is None:
            self.head = None
        else:
            temp = self.head
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end="--> ")
            temp = temp.next
        print("None")

new = Linkedlist()

for i in range(10):
    new.insert_at_end(i)

new.insert_at_index(3, 1000)

new.delete_at_index(5)

new.traverse()
