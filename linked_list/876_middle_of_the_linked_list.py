# https://leetcode.com/problems/middle-of-the-linked-list/

from typing import Optional
from ListNode import ListNode

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow