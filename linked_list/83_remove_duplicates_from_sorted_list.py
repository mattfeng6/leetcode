# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

from typing import Optional
from ListNode import ListNode

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Special Situation
        if head: return head

        dummy = head

        while head:
            if head.next and head.val == head.next.val:
                head.next = head.next.next
            else: head = head.next

        return dummy
