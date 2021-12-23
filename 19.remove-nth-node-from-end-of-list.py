#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#
from typing import Optional
# @lc code=start
# Definition for singly-linked list.



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def edgecases(self,head,n):
        pass
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pointer1=head
        pointer2=head
        for i in range(0,n):
            pointer2=pointer2.next
        
        if pointer2 is None:
            #!
            return head.next 
            pass
        
        while pointer2.next is not None:
            pointer1=pointer1.next
            pointer2=pointer2.next
        
        tmp=pointer1.next
        tmp=tmp.next
        pointer1.next=tmp
        
        return head
        
        
        # 1 2 3 4 5 6 7
        #n=3    |     |
         
        
        # 1 2 3 4 6 7
        
        
        
# @lc code=end

