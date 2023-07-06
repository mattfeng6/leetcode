# https://leetcode.com/problems/reorder-list/

from typing import Optional
from ListNode import ListNode

from collections import deque

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        queue = deque()
        
        curr = head
        while curr:
            queue.append(curr)
            curr = curr.next 

        while queue:
            left = queue.popleft()
            right = queue.pop() if queue else None

            temp = queue[0] if queue else None
            left.next = right
            if right: 
                right.next = temp

        return head
