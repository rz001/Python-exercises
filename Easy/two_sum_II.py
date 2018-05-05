"""
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
"""

class Solution(object):
    def twoSum(self, nums, target):
        sol = []
        lnums = len(nums)
        for i in xrange(0, lnums):
            for x in xrange(i+1, lnums):           
                if (nums[x] == target - nums[i]):
                    sol.append(i+1) 
                    sol.append(x+1)
                    return sol
                if (nums[i] == nums[x]) or (nums[i] > target) or (nums[x] >= target):
                    break
            
        return sol


s = Solution()
s = s.twoSum([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,3,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9], 5)
if s:
    print ("Indices for the given input are at position {} and {}".format(s[0],s[1]))        