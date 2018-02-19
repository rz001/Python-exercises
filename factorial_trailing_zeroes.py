"""
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.

Trailing 0s in n! = Count of 5s in prime factors of n!
                  = floor(n/5) + floor(n/25) + floor(n/125) + ....
"""

import math

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """

        zeroes = 0
        delta = 1
        i = 1
        while delta >= 1:
            delta = math.floor(n / math.pow(5, i))
            zeroes += delta
            i += 1

        return long(zeroes)

s = Solution()
sol = s.trailingZeroes(11)
if sol != None:
    print ("Number of factorial trailing zeroes is {} ".format(sol))



