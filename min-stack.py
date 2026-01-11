class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, item):
        self.stack.append(item)
        if not self.min_stack or item <= self.min_stack[-1]:
            self.min_stack.append(item)

    def pop(self):
        item = self.stack.pop()
        if item == self.min_stack[-1]:
            self.min_stack.pop()
        return item

    def get_min(self):
        if self.min_stack:
            return self.min_stack[-1]
        return None


# %%

mystack = MinStack()

mystack.push(1234)
mystack.push(890)
mystack.push(456)

print(mystack.get_min())
print(mystack.pop())
print(mystack.get_min())
# %%
