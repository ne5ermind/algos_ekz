class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.items[0]

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    # необязательно но при помощи эиой штуки можно смотреть все элементы разом
    def __str__(self):
        return ", ".join(map(str, self.items))


# %%

myqueue = Queue()
myqueue.enqueue(1)
myqueue.enqueue(3)
myqueue.enqueue(3)
myqueue.enqueue(7)
print(myqueue.peek())
myqueue.dequeue()
print(myqueue)
# %%
