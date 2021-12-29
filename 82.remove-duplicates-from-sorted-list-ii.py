#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# @lc code=start
# Definition for singly-linked list.

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        processed_nodes_tail_pointer=head
        current_processing_pointer=head
        while current_processing_pointer.next is not None:
            if current_processing_pointer.next.val == current_processing_pointer.val:
                pass
                
        
        
# @lc code=end

