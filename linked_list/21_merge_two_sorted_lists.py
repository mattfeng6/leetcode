# https://leetcode.com/problems/merge-two-sorted-lists/

from typing import Optional
from ListNode import ListNode

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        cur = dummy = ListNode(0)
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2

        if list1:
            cur.next = list1
        
        if list2:
            cur.next = list2

        return dummy.next

            
            
