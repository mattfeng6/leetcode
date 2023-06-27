# https://leetcode.com/problems/linked-list-cycle/

from typing import Optional
from ListNode import ListNode

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # Special Situation:
        # if head is null, no cycle for there is no element
        if not head: return False

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: return True
        return False