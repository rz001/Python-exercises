"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution(object):
    def twoSum(self, nums, target):
        sol = []
        i = 0
        x = 0
        for a in nums:
            for b in nums:
                if (i < x) and (b == target - a):
                    sol.append(i) 
                    sol.append(x)
                    return sol            
                x+=1
            i+=1
            x=0
        return sol
              
s = Solution()
s = s.twoSum([0, 43, 8, 2], 9)
if s:
    print ("Indices for the given input are at position {} and {}".format(s[0],s[1]))

#if len(s) == 2:
#    print ("Indices for the given input are at position {} and {}.".format(s[0], s[1]))
#else:
#    print ("No indices found.")