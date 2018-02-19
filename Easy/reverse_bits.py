"""
Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010 10010100 00011110 10011100), return 964176192 (represented in binary as 00111001011110000010100101000000).
                                                            00111001 01111000 00101001 01000000
Follow up:
If this function is called many times, how would you optimize it?

Related problem: Reverse Integer
"""

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):

        oribin = '{0:032b}'.format(n)
        print (oribin)
        reversebin = oribin[::-1]
        return int(reversebin, 2)



s = Solution()
sol = s.reverseBits(43261596)
if sol != None:
    print ("Reversed number is {}".format(sol))