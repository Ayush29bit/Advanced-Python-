class stack:
    
    def __init__(self):
        self.s = []
    
    def push(self,ele):
        self.s.append(ele)

    def peek(self):
        if len(self.s)==0:
            raise Exception("Stack is empty")
        else :
            return self.s[-1]
    
    def pop(self):
        if len(self.s)==0:
            raise Exception("Stack is empty")
        else :
            return self.s.pop()
