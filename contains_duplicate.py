"""
Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, 
and it should return false if every element is distinct.

"""
""" time limit exceeded
class Solution(object):
    def containsDuplicate(self, nums):
        
        :type nums: List[int]
        :rtype: bool
            
        counter = {}

        for i in nums:
            if i in counter.keys():
                return True
            else:
                counter.update({i:1})
        
        return False
"""

class Solution(object):
    def containsDuplicate(self, nums):
        
        #:type nums: List[int]
        #:rtype: bool

        return len(nums) != len(set(nums))


s = Solution()
sol = s.containsDuplicate([3, 4, 4, 6, 7])
if sol == True:
    print ("Given list contains duplicate.")