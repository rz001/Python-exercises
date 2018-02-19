"""
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = [[1], [1,1]]

        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1,1]]
        elif numRows > 2:
            for i in range(2, numRows):
                x = 1
                triangle.append([]) 
                triangle[i].insert(0,1)
                triangle[i].insert(len(triangle[i-1]),1)
                while  x < len(triangle[i-1]):     
                    triangle[i].insert(x, triangle[i-1][x-1] + triangle[i-1][x]) 
                    x += 1

            return triangle

s = Solution()
sol = s.generate(1)
if s:
    print ("Pascal's triangle is {} ".format(sol))