#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#
from typing import List, Optional
# @lc code=start
# Definition for singly-linked list.



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return self.mergeKLists_brutal(lists)
    def mergeKLists_brutal(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:        
        if self.edge_cases(lists) != False:
            return self.edge_cases(lists)
        
        head=ListNode()
        pointer=head
        while True:
        
            min=(10001,0)
            
            for i in range(len(lists)):
                if lists[i] is None:
                    continue
                if lists[i].val<min[0]:
                    min=(lists[i].val,i)
                    
            if min[0]==10001:
                break
            pointer.next=ListNode(lists[min[1]].val)
            lists[min[1]]=lists[min[1]].next
            pointer=pointer.next
        
        return head.next
        
        pass
    def edge_cases(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:   
        if len(lists)<=1: 
            return lists
        else:
            return False
        
        
        
# @lc code=end

