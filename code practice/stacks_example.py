class SortStack:
    def __init__(self):
        self.stack = []
        self.temp_stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty"

    def sort(self):
        temp_stack = []
        stack_copy = self.stack.copy()
        
        while stack_copy:
            temp = stack_copy.pop()
            while temp_stack and temp_stack[-1] > temp:
                stack_copy.append(temp_stack.pop())
            temp_stack.append(temp)
        return temp_stack

    def traverse(self):
        for item in self.stack:
            print(item)


data = SortStack()
print(data.is_empty())
for i in range(50,60):
    data.push(i)
for i in range(10):
    data.push(i)
print(data.is_empty())

