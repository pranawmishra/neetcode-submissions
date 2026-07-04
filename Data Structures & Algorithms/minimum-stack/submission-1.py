class MinStack:

    def __init__(self):
        self.stack = []
        # self.min_stack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        
    def pop(self) -> None:
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        min_val = 2**31
        for val in self.stack:
            min_val = min(min_val, val)

        return min_val
        
