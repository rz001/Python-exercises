"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1

Input: [3,0,1]
Output: 2
Example 2

Input: [9,6,4,2,3,5,7,0,1]
Output: 8

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

"""

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        next_i = 0

        if nums == []:
            return 0
      
        for i in nums:
            if next_i != i:
                return next_i
            next_i += 1

        if (next_i - nums[-1]) == 1:
            return next_i

s = Solution()
sol = s.missingNumber([])
if sol != None:
    print("The missing number is {}".format(sol))