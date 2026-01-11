class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()


def is_balanced(string):
    stack = Stack()
    mapping = {")": "(", "}": "{", "]": "["}
    for char in string:
        if char in mapping.values():
            stack.push(char)
        elif char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
    print(stack)
    return stack.is_empty()


# %%

mystack = Stack()

print(mystack.is_empty())

mystack.push(1)
mystack.push(3)
mystack.push(3)
mystack.push(7)

print(mystack.is_empty())
print(mystack.peek())
print(mystack.pop())
print(mystack.peek())

print(is_balanced("()()()()()()()())))))()((((()))"))
print(is_balanced("((asdihidash())osaduihoas)aiodjoas"))
# %%
