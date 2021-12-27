#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# @lc code=start
# Definition for singly-linked list.

class Solution:
    def edgecases(self,head,k):
        if k==0:
            return head
        if head is None:
            return head
        if head.next is None:
            return head
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k==0:
            return head
        if head is None:
            return head
        if head.next is None:
            return head
        endpointer=head
        newtailpointer=head
        step_forward=0
        

        while endpointer is not None and step_forward < k:

            endpointer=endpointer.next
            step_forward=step_forward+1

        
        if step_forward!=k:
            #return ListNode(step_forward)
            endpointer=head
            k=(k+1)%(step_forward)  
            step_forward=0      
            while endpointer is not None and step_forward < k:
            
                endpointer=endpointer.next
                step_forward=step_forward+1      



            # the length of the listnode is bigger than k. endpointer.next is still a listnode
            
        while endpointer.next is not None:
            endpointer=endpointer.next
            newtailpointer=newtailpointer.next
        
        #  endpointer reach the end of the listnode
        endpointer.next=head
        head=newtailpointer.next
        newtailpointer.next=None
                

  
                
        return head
            
            
            
            
            
        
        
# @lc code=end

