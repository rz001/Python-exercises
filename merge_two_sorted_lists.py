"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

"""
Web solution for linked list
class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

"""

#My solution for standard list
class Solution(object):
    def mergeTwoLists(self, l1, l2):

        lout = []
        lenl1 = len(l1)
        lenl2 = len(l2)
        i = 0
        x = 0
        while i < lenl1 and x < lenl2:
            if l2[x] < l1[i]:
                lout.append(l2[x])
                x += 1
            else:
                lout.append(l1[i])
                i += 1
        if i < x:
            lout = lout + l1[i:lenl1]
        elif i > x:
            lout = lout + l2[x:lenl2]
                
        return lout
        
      

sl = Solution()
res = sl.mergeTwoLists([1,2,3,4,5],[1,3,11,11])
if len(res) > 0:
    print ("Sorted list is {}".format(res))
