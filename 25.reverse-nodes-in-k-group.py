#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#
from typing import Optional
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def edgecases(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k==1:
            return head
        
        return False
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:    
        if self.edgecases(head,k)!=False:
            return self.edgecases(head,k)
        
        rootnode=ListNode()
        finished_pointer=rootnode
        end=False
        
        rootnode.next=head
        # root/finished->1>2>3>4>5
        
        while not end:
            
            pointer1=finished_pointer.next
            # r/f ->1/pointer1>2>3>4>5
            endpointer=pointer1
            # root/finish -> 1/pointer1>2/end

            
            for i in range(0,k):
                
                if endpointer==None:
                    end=True
                    break            
                endpointer=endpointer.next
            
            if end:
                break
            
            for i in range(0,k-1):
                
                modpointer=pointer1.next#2
                tmp=modpointer.next#345
                modpointer.next=finished_pointer.next
                pointer1.next=tmp   
                finished_pointer.next=modpointer         
            #21345
            
            finished_pointer.next=modpointer
            finished_pointer=pointer1
                    
        
        return rootnode.next
        
     
        
        
    def swapnode(self,node1,node2):
        pass
        
        
        
# @lc code=end

head=ListNode()
pointer=head
for i in [1,2,3,4,5]:
    pointer.next=ListNode(i)
    pointer=pointer.next

a=Solution()
print(a.reverseKGroup(head.next,3))