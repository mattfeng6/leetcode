# https://leetcode.com/problems/reverse-linked-list/
# https://www.youtube.com/watch?v=G0_I-ZF0S38

from typing import Optional
from ListNode import ListNode

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Two Pointers

        prev = None
        curr = head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev