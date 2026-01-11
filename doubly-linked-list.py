class DNode:
    def __init__(self, value, prev, next):
        self.value = value
        self.prev = prev
        self.next = next


class DLinkedList:
    def __init__(self):
        self.head = None
        self._len = 0

    def append(self, value):
        if not self.head:
            self.head = DNode(value, None, None)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = DNode(value, current, None)
        self._len += 1

    def del_by_id(self, key):
        if key > self._len - 1 or key < 0:
            raise IndexError(
                "ПОМОГИИИИИИИИИИИИИИИТЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕ"
            )
        elif key == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(key - 1):
                current = current.next
            current.next = current.next.next
        self._len -= 1

    def __str__(self):
        if self.head is None:
            return "Empty List"
        return ", ".join(str(val) for val in self)

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

    def len(self):
        return self._len


# %%

mylist = DLinkedList()

for i in (1, 9, 8, 4, 1):
    mylist.append(i)

print(mylist)
print(mylist.len())

mylist.del_by_id(3)
mylist.del_by_id(0)

print(mylist)
# %%
