"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        numsl = len(nums)
        x = numsl

        while i < numsl and i < x:
            if nums[i] == 0:
                del nums[i]
                nums.insert(x-1, 0) 
                i -= 1
                x -= 1
            i +=1

        return nums

s = Solution()
sol = s.moveZeroes([])
if sol != None:
    print ("New array with zeroes at the end is {}".format(sol))