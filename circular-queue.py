class CQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.head = 0
        self.tail = 0
        self.size = 0

    def enqueue(self, item):
        if self.size == self.capacity:
            raise OverflowError("Queue is full!")
        self.queue[self.tail] = item
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            raise IndexError("Queue is empty!")
        item = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return item


# %%

myqueue = CQueue(5)
myqueue.enqueue(1)
myqueue.enqueue(3)
myqueue.enqueue(3)
myqueue.enqueue(7)
myqueue.dequeue()

# %%
