"""
Reverse a singly linked list.

click to show more hints.

Hint:
A linked list can be reversed either iteratively or recursively. Could you implement both?

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_nexts = [None]

        while head != None and head != []:
            new_nexts.append(head)
            head = head.next
        
        i = len(new_nexts)
                 
        while i > 1:
            new_head = new_nexts[i-1]  
            new_head.next = new_nexts[i-2]
            new_head = new_head.next
            i -= 1
            
        final_head = new_nexts[-1]
        return final_head 