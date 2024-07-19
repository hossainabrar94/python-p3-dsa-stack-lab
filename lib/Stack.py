class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    @property
    def limit(self):
        return self._limit
    @limit.setter
    def limit(self, limit):
        if len(self.items) > limit:
            raise ValueError('The items stack has reached its limit')
        self._limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if not self.full():
            self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        return None

    def peek(self):
        pass
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) >= self.limit

    def search(self, target):
        for item in self.items:
            if item == target:
                return (len(self.items) - 1 - self.items.index(item))
        return -1