# https://leetcode.com/problems/palindrome-linked-list/

from typing import Optional
from ListNode import ListNode

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        # l = []
        # while head:
        #     l.append(head.val)
        #     head = head.next
        # return l == l[::-1]

        # Two Pointers

        fast, slow  = head,head    
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
    
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        while head and prev:
            if head.val != prev.val:
                return False
            else:
                head = head.next
                prev = prev.next
        return True