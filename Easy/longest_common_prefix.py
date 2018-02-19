"""

Write a function to find the longest common prefix string amongst an array of strings.

"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        cl = 0
        commons = ''
        sols = ''
        if len(strs) > 0:
            commons = strs[0] 
            cl = len(commons)
            for i in range(1, len(strs)):
                if cl >= len(strs[i]):
                    cl = len(strs[i])
                csl = 0
                for x in range(0, cl):
                    if commons[x] == strs[i][x]:
                        csl = x + 1
                    else:
                        break
                cl = csl
        return commons[0:cl]

s = Solution()

coms = s.longestCommonPrefix(['a','a','b'])

print (coms)