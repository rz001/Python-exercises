"""
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
            
        if s == '' and t == '':
            return True

        sd = {}
        td = {}
        
        for i in s:
            if i not in sd.keys():
                sd.update({i:1})
            else:
                sd[i] += 1
        
        for x in t:
            if x not in td.keys():
                td.update({x:1})
            else:
                td[x] += 1
        
        for r, u in sd.items():
            if (r not in td.keys()) or (td[r] != u):
                return False
        
        return True 



s = Solution()
sol = s.isAnagram('', '')
if sol == True:
    print ("t is anagram of s.")


