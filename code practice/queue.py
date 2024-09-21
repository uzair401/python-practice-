class CircularQueue:
    def __init__(self,size) -> None:
        self.queue = []
        self.size = size
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def is_full(self):
        return len(self.queue) == self.size
    
    def enqueue(self,data):
        if not self.is_full():
            self.queue.append(data)
        else:
            print("Queue is Full")

    def dequeue(self):
        if not self.is_empty():
            self.queue.pop(0)
        else:
            print("Queue is Empty")

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
    
cq = CircularQueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)  # Queue is now full
cq.dequeue()    # Removes 10
cq.enqueue(60)  # Inserts 60 into the queue
cq.peek()       # Returns 20 (front of the queue)
cq.enqueue(70)  # Queue is full, cannot add 70



# class queue:
#     def __init__(self) -> None:
#         self.queue = []
    
#     def is_empty(self):
#         return len(self.queue) == 0
    
#     def enqueue(self,data):
#         self.queue.append(data)
#     def dequeue(self):
#         self.queue.pop(0)
#     def first_element(self):
#         if not self.is_empty():
#             return self.queue[0]
#         else:
#             print('queue is empty')
#     def traverse(self):
#         for item in self.queue:
#             print(item, end = " ")
#     def size(self):
#         return len(self.queue)
# e = queue()

# # print(e.is_empty())
# print(e.size())
# e.enqueue(100)
# e.enqueue(500)
# e.enqueue(200)
# print(e.size())
# e.traverse()