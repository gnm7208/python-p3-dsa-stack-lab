class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = list(items)
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            raise IndexError("Stack is full")

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        return None
    
    def size(self):
        return len(self.items)

    def full(self):
        return self.size() >= self.limit

    def search(self, target):
        if target in self.items:
            reversed_stack = self.items[::-1]
            return reversed_stack.index(target)
        return -1