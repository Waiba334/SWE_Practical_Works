# postfix expressions.
def evaluate_postfix(expression):
    stack = []
    
    for token in expression.split():
        if token.isdigit():  
            stack.append(int(token))
        else: 
            operand2 = stack.pop()
            operand1 = stack.pop()
            
            if token == '+':
                stack.append(operand1 + operand2)
            elif token == '-':
                stack.append(operand1 - operand2)
            elif token == '*':
                stack.append(operand1 * operand2)
            elif token == '/':
                stack.append(int(operand1 / operand2))  
    
    return stack.pop()

expression = "3 4 + 2 * 7 /"
print(f"Result of '{expression}':", evaluate_postfix(expression))  # Outputs: 2

# Implementing a Queue Using Two Stacks
class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if self.stack2:
            return self.stack2.pop()
        else:
            raise IndexError("Queue is empty")

queue = QueueUsingStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue()) 
print(queue.dequeue()) 

#Basic Task Scheduler Using a Queue
from collections import deque

class TaskScheduler:
    def __init__(self):
        self.queue = deque()
    
    def add_task(self, task):
        self.queue.append(task)
    
    def process_tasks(self):
        while self.queue:
            task = self.queue.popleft()
            print("Processing:", task)

scheduler = TaskScheduler()
scheduler.add_task("task1")
scheduler.add_task("task2")
scheduler.add_task("task3")
scheduler.process_tasks()

#Infix to Postfix Conversion Using a Stack
def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    stack = []
    output = []
    
    for token in expression.split():
        if token.isalnum():  
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  
        else:  
            while (stack and stack[-1] != '(' and 
                   precedence.get(token, 0) <= precedence.get(stack[-1], 0)):
                output.append(stack.pop())
            stack.append(token)
    
    while stack:
        output.append(stack.pop())
    
    return ' '.join(output)

expression = "3 + 4 * 2 / ( 1 - 5 )"
print("Postfix:", infix_to_postfix(expression))