"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"

"""
import math

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """

        title = ''

        alphabet = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H', 8:'I', 9:'J', 10:'K',
         11:'L', 12:'M', 13:'N', 14:'O' ,15:'P', 16:'Q', 17:'R', 18:'S', 19:'T', 20:'U', 21:'V', 22:'W', 23:'X', 24:'Y', 25:'Z'}

        n = n - 1

        while n >= 0:
            title = alphabet[int (n % 26)] + title
            n = n // 26 - 1 
                     
        return title

s = Solution()
sol = s.convertToTitle(701)
if sol != None:
    print ("Column title is {} ".format(sol))