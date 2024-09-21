# reversing a string using stack
class Stack:
    def __init__(self) -> None:
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty"

    def top(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty"

    def reverse(self):
        reversed_list = []
        while not self.is_empty():
            reversed_list.append(self.pop())
        return ''.join(reversed_list)


st = Stack()
for char in "Khan":
    st.push(char)
print(st.reverse())

