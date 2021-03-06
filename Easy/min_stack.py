"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.

"""
import sys

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = [{}]
      
        
    def top(self):
        """
        :rtype: int
        """
        for key in self.stack[0].keys():
            return key
    
        
    def getMin(self):
        """
        :rtype: int
        """
        for val in self.stack[0].values():
            return val
        
    
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        
        y = self.getMin()
        if x < y or self.stack == [{}]:
            self.stack.insert(0,{x:x})
        else:
            self.stack.insert(0,{x:self.getMin()})
      
    
    def pop(self):
        """
        :rtype: void
        """
        for key in self.stack[0].keys():
            self.stack.pop(0)
            return key
    



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print (minStack.getMin()) #  --> Returns -3.
minStack.pop()
print (minStack.top()) #     --> Returns 0.
print (minStack.getMin())#   --> Returns -2.