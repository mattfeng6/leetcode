# https://leetcode.com/problems/swap-nodes-in-pairs/
# https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0024.%E4%B8%A4%E4%B8%A4%E4%BA%A4%E6%8D%A2%E9%93%BE%E8%A1%A8%E4%B8%AD%E7%9A%84%E8%8A%82%E7%82%B9.md

from typing import Optional
from ListNode import ListNode

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(next=head)
        curr = dummy

        while curr.next and curr.next.next:
            temp = curr.next
            rest = curr.next.next.next

            curr.next = temp.next
            curr.next.next = temp
            temp.next = rest
            curr = temp
        return dummy.next
        
