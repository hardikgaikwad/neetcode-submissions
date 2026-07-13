class MinStack:

    def __init__(self):
        self.stk = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        return None

    def pop(self) -> None:
        if not self.stk:
            pass
        self.stk.pop()
        return None

    def top(self) -> int:
        if not self.stk:
            pass
        return self.stk[-1]
        

    def getMin(self) -> int:
        if not self.stk:
            pass
        return min(self.stk)
