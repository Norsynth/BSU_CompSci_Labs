class Stack: #good at working with data enclosed with symbols
    
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self,n): #adjusted
        return self.items[len(self.items)-1-n]

    def size(self):
        return len(self.items)

    def show(self): #added
        return self.items
