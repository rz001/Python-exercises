"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5
"""

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        inword = False
        lastword = 0
        x = 0

        for i in range(0, len(s)):
            if s[i] != ' ':
                inword = True
                x += 1
            elif inword == True:
                lastword = x
                inword = False
                x = 0
        
        if x == 0:
            return lastword
        else:
            return x 



s = Solution()
sol = s.lengthOfLastWord("abec   ")
if sol != None:
    print ("The last word length is {}".format(sol))