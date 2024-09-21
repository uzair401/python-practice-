class deque:
    def __init__(self) -> None:
        self.queue = []

    def add_front(self, data):
        self.queue.insert(0, data)
    def add_back(self,data):
        self.queue.append(data)

    def remove_back(self):
        self.queue.pop()
    def remove_back(self):
        self.queue.pop(0)
    def peek_front(self):
        return self.queue[0]
    def peek_front(self):
        return self.queue[-1]
    def traverse(self):
        for item in self.queue:
            print(f"Item: {item}")
q = deque()
q.add_back(100)
q.add_back(134)
q.add_back(4522)
q.add_front(10)
q.add_front(1234)
q.traverse()
