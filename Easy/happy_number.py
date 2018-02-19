"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, 
and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. 
Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        nsum = 0
        seen_numbers = set([n])
        
        while n != 1:
            nstring = str(n)
            for i in nstring:
                nsum += pow(int(i), 2)

            if nsum not in seen_numbers:
                n = nsum
                seen_numbers.add(nsum) 
                nsum = 0
            else:
                break

        if n == 1:
            return True
        else:
            return False


s = Solution()
sol = s.isHappy(7)
if sol == True:
    print ("This numer is happy.")