# https://leetcode.com/problems/remove-linked-list-elements/

from typing import Optional
from ListNode import ListNode

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        dummy1 = ListNode()
        dummy2 = dummy1

        dummy1.next = head

        while dummy1.next:
            if dummy1.next.val == val:
                dummy1.next = dummy1.next.next
            else: dummy1 = dummy1.next
       
        return dummy2.next


