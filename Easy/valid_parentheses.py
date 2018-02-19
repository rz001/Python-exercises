"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        top = ''
        for i in range(0, len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.insert(0, s[i])
            if len(stack) == 0:
                return False
            if s[i] == ')':
                top = stack.pop(0)
                if top != '(':
                    return False 
            elif s[i] == '}':
                top = stack.pop(0)
                if top != '{':
                    return False 
            elif s[i] == ']':
                top = stack.pop(0)
                if top != '[':
                    return False 
               

        if len(stack) == 0 and len(s) > 0:
            return True
        else:
            return False 


sl = Solution()
res = sl.isValid('')
if res:
    print ("Given String is valid.")
else:
    print ("Given String is INvalid.")
