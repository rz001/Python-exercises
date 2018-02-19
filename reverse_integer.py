"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output:  321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range. 
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""
import math

class Solution(object):
    def reverse(self,num):
        rnum = 0
        x = 0
        firstnonzero = False
        anum = abs(num)
        for i in xrange(10, 0, -1): 
            ordern = (anum % pow(10,i) // pow(10,i-1))
            if ordern != 0:
                firstnonzero = True
                rnum = rnum + ordern*pow(10,x)
            if firstnonzero:
                x+=1
        if rnum > pow(2,31):
            return 0
        elif num < 0:
            return -1*rnum
        else:
            return rnum

sol = Solution()
revint = sol.reverse(-931040)
print (revint)



