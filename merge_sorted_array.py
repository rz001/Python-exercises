"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. 
The number of elements initialized in nums1 and nums2 are m and n respectively.

"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = nums1[:m]
        nums2[:] = nums2[:n]

        if m == 0:
            nums1 = nums2
            m = n
        elif n == 0:
            pass
        else:    
            nums1 = nums1 + nums2
            lnums1 = m + n
            print (nums1)
            for i in range(0, lnums1):
                for x in range(i, lnums1):
                    if nums1[i] > nums1[x]:
                        nums1[i], nums1[x] = nums1[x], nums1[i]

        return nums1


s = Solution()
nums11 = [0, 1, 2, 4, 11]
nums22 = [10, 11, 3]
res = s.merge(nums11, 5, nums22, 3)
print ("Merged list is {}".format(res))