"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        x = len(s) - 1
        while i < len(s) and x > 0:
            if not s[i].isalnum() and not s[x].isalnum():
                x -= 1
                i += 1
                continue
            elif not s[i].isalnum(): 
                i += 1
                continue
            elif not s[x].isalnum():
                x -= 1
                continue
            if s[i].lower() != s[x].lower():
                return False     
            x -= 1
            i += 1
        
        return True

s = Solution()
sol = s.isPalindrome('')
if sol:
    print ("Provided string is palindrome.")