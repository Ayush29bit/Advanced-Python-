"""
Queue is a linear data structure that follows the First In First Out (FIFO) principle.
In a queue, the first element added (enqueued) to the queue is the first one to be removed (dequeued).

The main operations of a queue are:
1. Enqueue: Add an element to the rear of the queue.
2. Dequeue: Remove the front element from the queue.
3. Peek (or Front): Retrieve the front element without removing it.
"""

class Queue:
    def __init__(self, capacity : int):
        self.capacity = capacity
        self.queue = []

    def is_full(self) -> bool:
        return len(self.queue) == self.capacity
    
    def is_empty(self) -> bool:
        return len(self.queue) == 0
    
    def enqueue(self, item):
        if self.is_full():
            raise Exception("Queue is full")
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue.pop(0)
    
    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue[0]
    
"""
Methods:
1. is_full(): Checks if the queue is full.
2. is_empty(): Checks if the queue is empty.
3. enqueue(item): Adds an item to the rear of the queue.
4. dequeue(): Removes and returns the front item from the queue.
5. peek(): Returns the front item without removing it.
"""

"""
Example Usage:
queue = Queue(5)
queue.enqueue(10)
queue.enqueue(20)
print(queue.peek())  # Output: 10
print(queue.dequeue()) # Output: 10
print(queue.dequeue()) # Output: 20
print(queue.is_empty()) # Output: True
"""
