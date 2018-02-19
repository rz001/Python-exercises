"""
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer '11' has binary representation 00000000000000000000000000001011, so the function should return 3.

"""

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        allbits = '{0:032b}'.format(n)
        
        return allbits.count('1')

s = Solution()
sol = s.hammingWeight(123234)
if sol != None:
    print ("The number of 1 bits is {}".format(sol))