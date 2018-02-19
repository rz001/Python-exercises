"""
Given an array of size n, find the majority element. The majority element is the element that appears more than [n/2] times.

You may assume that the array is non-empty and the majority element always exist in the array.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.

"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        majority = len(nums) // 2
        elements = {}

        for i in range (0, len(nums)):
            if nums[i] in elements.keys():
                elements[nums[i]] += 1
            else:
                elements.update({nums[i]:1})
            if elements[nums[i]] > majority:
                    return nums[i]
                        
        return None

sl = Solution()
res = sl.majorityElement([5])

if res:
    print ("The majority element is {}".format(res))