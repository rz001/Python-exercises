"""
Given a non-negative index k where k <= 33, return the kth  index row of the Pascal's triangle.

Note that the row index starts from 0.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?

"""

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        triangle = [[1], [1,1]]
       
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        elif rowIndex > 1:
            for i in range(2, rowIndex+1):
                x = 1
                triangle.append([]) 
                triangle[i].insert(0,1)
                triangle[i].insert(len(triangle[i-1]),1)
                while  x < len(triangle[i-1]):     
                    triangle[i].insert(x, triangle[i-1][x-1] + triangle[i-1][x]) 
                    x += 1
        
            return triangle[rowIndex]

k = 4
s = Solution()
sol = s.getRow(k)
if sol:
    print ("Pascal triangle {}th/rd row is {}".format(k, sol))

