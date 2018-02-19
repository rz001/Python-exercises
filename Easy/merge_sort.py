"""
Description:
Merge sort
"""

class Solution(object):
    def mergeSort(self, arr):

        if len(arr)>1:
            mid = len(arr)//2
            lefthalf = arr[:mid]
            righthalf = arr[mid:]

            self.mergeSort(lefthalf)
            self.mergeSort(righthalf)

            i=0
            j=0
            k=0
            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i] < righthalf[j]:
                    arr[k]=lefthalf[i]
                    i=i+1
                else:
                    arr[k]=righthalf[j]
                    j=j+1
                k=k+1

            while i < len(lefthalf):
                arr[k]=lefthalf[i]
                i=i+1
                k=k+1

            while j < len(righthalf):
                arr[k]=righthalf[j]
                j=j+1
                k=k+1

        return arr


s = Solution()
sol = s.mergeSort([3,5,2,1,0,8])
if sol != None:
    print ("The sorted array is {}".format(sol))      
        
