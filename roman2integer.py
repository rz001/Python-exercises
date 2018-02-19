
"""
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
"""

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        last = ''
        for n in s:
            if n == 'M' and last == 'C':
                num = num + 800
                last = 'M'             
            elif n == 'M':
                num += 1000
                last = 'M'
            elif n == 'D' and last == 'C':
                num = num + 300
                last = 'D'
            elif n == 'D':
                num += 500
                last = 'D'
            elif n == 'C' and last == 'X':
                num = num + 80
                last = 'C'          
            elif n == 'C':
                num += 100
                last = 'C'
            elif n == 'L' and last == 'X':
                num = num + 30
                last = 'L'          
            elif n == 'L':
                num += 50
                last = 'L'          
            elif n == 'X' and last == 'I':
                num = num + 8
                last = 'X'
            elif n == 'X': 
                num += 10
                last = 'X'
            elif n == 'V' and last == 'I':
                num = num + 3
                last = 'V'              
            elif n == 'V': 
                num += 5
                last = 'V'              
            elif n == 'I': 
                num += 1
                last = 'I'  

        return num


romann = 'MMXIV'
s = Solution()
s = s.romanToInt(romann)
if s:
    print ("{} is arabic representation of roman number {}".format(s,romann))

