"""
Description:
Insertion sort
"""

class Solution(object):
    def insetionSort(self, arr):

        for i in range(1, len(arr)):
            
            cvalue = arr[i]
            x = i

            while x > 0 and arr[x-1] > cvalue:
                    arr[x] = arr[x-1]
                    x -= 1
            arr[x] = cvalue

        return arr



s = Solution()
sol = s.insetionSort([3,5,2,1,0,8])
if sol != None:
    print ("The sorted array is {}".format(sol))      
        
