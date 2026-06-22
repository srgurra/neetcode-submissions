class MinStack:

    def __init__(self):
        self.stack=[]
        self.mins=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mins:
            self.mins.append(len(self.stack)-1)
        elif self.stack[self.mins[-1]]>val:
            self.mins.append(len(self.stack)-1)


    def pop(self) -> None:
        
        if self.mins[-1]== len(self.stack)-1:
            self.mins.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.stack[self.mins[-1]]
        
