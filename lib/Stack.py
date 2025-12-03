class Stack:
    """A Stack implementation using a list as the underlying data structure."""

    def __init__(self, items = [], limit = 100):
        """Initialize stack with optional items and limit."""
        self.items = list(items)
        self.limit = limit

    def isEmpty(self):
        # Check if stack is empty
        return len(self.items) == 0

    def push(self, item):
        # Add item to top of stack if not full
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            raise IndexError("Stack is full")

    def pop(self):
        # Remove and return top item from stack
        if not self.isEmpty():
            return self.items.pop()
        return None

    def peek(self):
        # Return top item without removing it
        if not self.isEmpty():
            return self.items[-1]
        return None
    
    def size(self):
        # Return number of items in stack
        return len(self.items)

    def full(self):
        # Check if stack is at capacity
        return self.size() >= self.limit

    def search(self, target):
        # Find distance from top of stack to target element
        if target in self.items:
            reversed_items = self.items[::-1]
            return reversed_items.index(target)
        return -1
