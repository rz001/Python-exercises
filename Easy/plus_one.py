"""
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits.insert(0, 0) 
        digitsl = len(digits)

        sum = 0
    
        for i in range(digitsl-1, -1, -1):
            sum = digits[i] + 1
            if sum <= 9:
                digits[i] = sum
                if digits[0] == 0:
                    del digits[0]
                return digits
            if sum == 10:
                digits[i] = 0
                sum = 0


sl = Solution()
res = sl.plusOne([2,9,9])

if len(res) > 0:
    print ("The integer plus one is {}".format(res))