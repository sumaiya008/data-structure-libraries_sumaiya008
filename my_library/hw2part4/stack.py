#program to implement a stack using queue

from collections import deque

class Stack(object):
    def __init__(self):
        """
        Create an empty stack here.
        """
        self.q = deque()

# push element in stack
     def push(self, x):
        """
        @param x, an int
        return nothing
        """
        self.q.append( x )

     def pop(self):
        """
        pop one item
        return nothing
        """
        queueLen = len(self.q)
        for i in range(queueLen-1):
            x = self.q.popleft()
            self.q.append(x)
        self.q.popleft()  

    def peek(self):
        """
        return top element
        """
        if self.q.is_empty():
            raise IndexError('Stack have no element')
            else:
        for i in range(len(self.q)):
            x = self.q.popleft()
            self.q.append(x)
        return x