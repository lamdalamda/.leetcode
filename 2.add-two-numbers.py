#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        tenplus=0
        init_node=ListNode()
        init_node.val=(l1.val+l2.val)%10
        tenplus=int((l1.val+l2.val)/10)
        this_node=init_node
        while (l1.next!=None or l2.next!=None) or tenplus!=0:
            if l1.next==None:
                l1.next=ListNode(0)
            if l2.next==None:
                l2.next=ListNode(0)


            this_node.next=ListNode((l1.next.val+l2.next.val+tenplus)%10)
            tenplus=int((l1.next.val+l2.next.val+tenplus)/10)
            this_node=this_node.next
                
            l1=l1.next
            l2=l2.next
            
        return init_node                

        result=1
        tenplus=0
        
        

        for i in range(0,min(len(l1),len(l2))):
            
            result.append((l1[i]+l2[i]+tenplus)%10)            
            tenplus=int((l1[i]+l2[i]+tenplus)/10)
        if len(l1)>len(l2):
            for i in range(len(l2),len(l1)):
                result.append((l1[i]+tenplus)%10)
                tenplus=int((l1[i]+tenplus)/10)
        if len(l1)<len(l2):
            for i in range(len(l1),len(l2)):
                result.append((l2[i]+tenplus)%10)
                tenplus=int((l2[i]+tenplus)/10)       
        if tenplus==1:
            result.append(1)
        return result         

# @lc code=end

