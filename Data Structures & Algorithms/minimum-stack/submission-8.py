class MinStack:

    def __init__(self):
        self.stack = []
        # self.min_stack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        # if len(self.min_stack) == 0:
        #     self.min_stack.append(val)
        # else:
        #     min_val = min(val)
        
    def pop(self) -> None:
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return sorted(self.stack)[0]
        # min_val = 2**31
        # for val in self.stack:
        #     min_val = min(min_val, val)

        # return min_val
        
