class Task:
    def __init__(self, name, priority) -> None:
        self.name = name 
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

    def __repr__(self):
        return f"Task('{self.name}', {self.priority})"


class PriorityQueue:
    def __init__(self) -> None:
        self.queue = []

    def enqueue(self, task):
        self.queue.append(task)
        self.queue.sort()

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        else:
            print("Queue is empty")

    def traverse(self):
        for item in self.queue:
            print(f"Item: {item}")


q = PriorityQueue()
q.enqueue(Task("Casandra", 1))
q.enqueue(Task("Nova", 2))
q.enqueue(Task("James", 10))
q.traverse()