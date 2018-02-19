"""

Implement int sqrt(int x).

Compute and return the square root of x.

x is guaranteed to be a non-negative integer.


Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we want to return an integer, the decimal part will be truncated.

"""

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 3:
        	return 1
        delta = 0.1
        y = 1.0
        while abs(delta) > 0.01:
        	y = 0.5 * (y + x / y)
        	delta = x - (y * y)
        	print(delta)
        	
        return int(y)
        
        
s = Solution()
res = s.mySqrt(13538)
print ("Square root is {}".format(res))

