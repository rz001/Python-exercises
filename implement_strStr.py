"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        lh = len(haystack)
        ln = len(needle)
        lcommon = 0
        i = 0
        x = 0
        if ln == 0:
            return 0
        else:
            while i < lh and x < ln:
                if haystack[i] == needle[x]:
                    lcommon += 1
                    if lcommon == 1:
                        begini = i
                    if lcommon == ln and x == ln-1:
                        return begini 
                    x += 1
                else:
                    if lcommon < ln:
                        i = i - lcommon 
                    x = 0
                    lcommon = 0
                i += 1
        
        return -1        
                          


sl = Solution()
res = sl.strStr("mississippi","sipp")

if res >= 0:
    print ("Needle was found at index {}".format(res))
elif res == -1:
    print ("Needle was not found")        