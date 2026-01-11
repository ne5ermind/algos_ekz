from abc import ABC, abstractmethod


class Heap(ABC):
    def __init__(self):
        self.heap = []

    def _parent_index(self, index):
        if index == 0:
            return None
        return (index - 1) // 2

    def _left_child_index(self, index):
        return 2 * index + 1

    def _right_child_index(self, index):
        return 2 * index + 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        self._shift_up(len(self.heap) - 1)

    def peek(self):
        if self.is_empty():
            return None
        return self.heap[0]

    def is_empty(self):
        return len(self.heap) == 0

    def __str__(self):
        return ", ".join(map(str, self.heap))

    @abstractmethod
    def _shift_up(self, index):
        pass

    @abstractmethod
    def _shift_down(self, index):
        pass


class MinHeap(Heap):
    def __init__(self):
        super().__init__()

    def _shift_up(self, index):
        parent_index = self._parent_index(index)
        while parent_index is not None and self.heap[index] < self.heap[parent_index]:
            self._swap(index, parent_index)
            index = parent_index
            parent_index = self._parent_index(index)

    def _shift_down(self, index):
        min_child_index = index
        while True:
            left_child_index = self._left_child_index(index)
            right_child_index = self._right_child_index(index)

            if (
                left_child_index < len(self.heap)
                and self.heap[left_child_index] < self.heap[min_child_index]
            ):
                min_child_index = left_child_index

            if (
                right_child_index < len(self.heap)
                and self.heap[right_child_index] < self.heap[min_child_index]
            ):
                min_child_index = right_child_index

            if min_child_index != index:
                self._swap(index, min_child_index)
                index = min_child_index
            else:
                break


# %%

heap = MinHeap()
heap.insert(3)
heap.insert(1)
heap.insert(7)
heap.insert(3)
print(heap)
print(heap.peek())
# %%
