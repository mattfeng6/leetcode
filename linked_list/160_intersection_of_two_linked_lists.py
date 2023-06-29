# https://leetcode.com/problems/intersection-of-two-linked-lists/
# https://leetcode.com/problems/intersection-of-two-linked-lists/solutions/2561582/python-91-66-faster-simplest-solution-with-explanation-beg-to-adv-linked-list/

from typing import Optional
from ListNode import ListNode

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        # Special Situation
        if not headA or not headB:
            return None
        
        # Time Complexity: O(m + n)
        # Space Complexity: O(1)

        currA, currB = headA, headB
        while currA != currB:
            currA = headB if currA is None else currA.next
            currB = headA if currB is None else currB.next

            # traverse the other line to avoid the length diff

        return currA
