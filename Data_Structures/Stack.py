"""
Stack is a linear data structure that follows the Last In First Out (LIFO) principle.
In a stack, the last element added (pushed) to the stack is the first one to be removed (popped).
The main operations of a stack are:
1. Push: Add an element to the top of the stack.
2. Pop: Remove the top element from the stack.
3. Peek (or Top): Retrieve the top element without removing it.
"""

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

"""
In this implementation, we define a Stack class with an internal list to store the elements of the stack.
The push method adds an element to the top of the stack, the peek method retrieves the top element without removing it, and the pop method removes and returns the top element from the stack.
We also include error handling to raise an exception if we try to peek or pop from an empty stack.
"""

"""Example usage:"""

my_stack = stack()
my_stack.push(10)
my_stack.push(20)
print(my_stack.peek())  # Output: 20
print(my_stack.pop())   # Output: 20
print(my_stack.peek())  # Output: 10

"""Applications of Stack:
1. Expression Evaluation: Stacks are used to evaluate expressions, especially in infix, postfix, and prefix notations.
2. Backtracking: Stacks are used in algorithms that involve backtracking, such as depth-first search (DFS) in graphs and solving puzzles like the N-Queens problem.
3. Function Call Management: Stacks are used to manage function calls in programming languages, where each function call creates a new stack frame.
4. Undo Mechanism: Stacks can be used to implement undo functionality in applications, where the last action can be reversed by popping it from the stack.
5. Syntax Parsing: Stacks are used in compilers and interpreters to parse syntax and manage nested structures like parentheses, brackets, and braces."""