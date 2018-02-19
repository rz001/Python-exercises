"""
Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        origlen = len(nums)
        newlen = origlen
        i = 0
        while i >= 0 and i < (newlen-1):
            if nums[i] == nums[i+1]:
                del nums[i+1]
                newlen -= 1
            else:
                i += 1
        print ("New sorted array is {}".format(nums))  
        return newlen 



sl = Solution()
res = sl.removeDuplicates([2,33,33,33,456,456,456,1000,1000])

print ("Length of the new sorted array is {}".format(res))