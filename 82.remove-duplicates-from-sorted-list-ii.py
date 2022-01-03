
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
        if head is None:
            return None
        if head.next is None:
            return head
        return self.deleteDuplicates_recursive(head)
    def deleteDuplicates_recursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head
        if head.next.val==head.val:
            pointer=head
            while pointer.next is not None:
                if pointer.next.val==pointer.val:
                    pointer=pointer.next
                else:
                    return self.deleteDuplicates_recursive(pointer.next)
        else:
            remake=head
            remake.next=self.deleteDuplicates_recursive(head.next)
            return remake
        
        
    def deleteDuplicates1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # wrong
        root=ListNode()
        root.next=head
        
        processed_nodes_tail_pointer=root#所有已遍历的节点中，最后一个没有重复的节点
        current_processing_pointer=head# 正在遍历的节点
        current_processing_node_value=current_processing_pointer.val
        duplicating=False
        
        
        while current_processing_pointer.next is not None:
            if current_processing_pointer.next.val==current_processing_node_value:
                current_processing_pointer=current_processing_pointer.next
                duplicating=True
            else:#current=1,current.next=2
                
                if duplicating:
                    current_processing_pointer=current_processing_pointer.next# current jump from 1 to 2
                    
                    processed_nodes_tail_pointer.next=current_processing_pointer # all node=1 is omitted
                
                else:
                    #processed_nodes_tail_pointer=current_processing_pointer
                    current_processing_pointer=current_processing_pointer.next
                
            
        return root.next
                    
         
# @lc code=end

