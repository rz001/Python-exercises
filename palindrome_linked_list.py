
"""
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        fast = slow = head
        # find the mid node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # reverse the second half
        node = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt
        # compare the first and second half nodes
        while node: # while node and head:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True
"""
Not working
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        heads = []
        half = 0
        maybeis_even = maybeis_odd = False  
        i = 0
        while head != None and head.next != None:
            
            if head.val == head.next.val:
                maybeis_even = True
                half = i
            if heads[-1] == head.next.val:
                maybeis_odd = True
                half = i-1
            if maybeis_even or maybeis_odd:    
                if heads[-(i-half)] != head:
                     maybeis_even = maybeis_odd = False   
            i += 1
            heads.append(head)

        return  maybeis_even or maybeis_odd
"""