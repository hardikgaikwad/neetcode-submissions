class MinStack:

    def __init__(self):
        self.stk = []
        self.min = float('inf')

    def push(self, val: int) -> None:
        if not self.stk:
            self.stk.append(0)
            self.min = val
        else:
            self.stk.append(val-self.min)
            self.min = min(self.min, val)

    def pop(self) -> None:
        if not self.stk:
            return
        
        pop = self.stk.pop()

        if pop < 0:
            self.min = self.min - pop

    def top(self) -> int:
        top = self.stk[-1]
        if top > 0:
            return top + self.min
        else:
            return self.min
    
    def getMin(self) -> int:
        return self.min    
