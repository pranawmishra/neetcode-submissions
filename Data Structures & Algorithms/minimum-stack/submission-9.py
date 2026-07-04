class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_stack) == 0:
            self.min_stack.append(val)
        else:
            min_val = min(self.min_stack[-1], val)
            self.min_stack.append(min_val)
        
    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        # min_val = 2**31
        # for val in self.stack:
        #     min_val = min(min_val, val)

        # return min_val
        
