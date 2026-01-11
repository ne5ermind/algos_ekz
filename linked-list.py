class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self._length = 0

    def append(self, value):
        if self.head is None:
            self.head = Node(value, None)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value, None)
        self._length += 1

    def prepend(self, value):
        if self.head is None:
            self.head = Node(value, None)
        else:
            new_node = Node(value, self.head)
            self.head = new_node

    def len(self):
        return self._length

    def __str__(self):
        if self.head is None:
            return "Empty List"
        return ", ".join(str(val) for val in self)

    def del_by_id(self, key):
        if key > self._length - 1 or key < 0:
            raise IndexError("Index our of range")
        elif key == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(key - 1):
                current = current.next
            current.next = current.next.next
        self._length -= 1

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next


# %%

mylist = LinkedList()

for i in (1, 9, 8, 4, 1):
    mylist.append(i)

print(mylist)
print(mylist.len())

mylist.del_by_id(3)
mylist.del_by_id(0)
mylist.prepend(100)

print(mylist)
# %%
