#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def swap(self,node1,node2):
        temp=node1.val
        node1.val=node2.val
        node2.val=temp
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        link_length=1
        pointer=head

        while pointer.next:
            pointer=pointer.next
            link_length+=1
            
        if link_length==1:
            return head
        pointer1=head
        pointer2=head.next
        if link_length==2:
            if pointer1.val>pointer2.val:
                self.swap(pointer1,pointer2)
            return head
        
        # 1st run, sort 2 element
        problem_size=2
        if link_length%2==0:
            for i in range(0,link_length/2):
                if pointer1.val>pointer2.val:
                    self.swap(pointer1,pointer2)
                pointer1=pointer2.next
                pointer2=pointer1.next
        
        
        #2nd run, sort 4 element
        link_length=link_length/2
        problem_size=problem_size*2
        pointer1=head
        pointer2=head
        if link_length%2==0:
            for i in range(0,problem_size/2):
                pointer2=pointer2.next
            for i in range(0,link_length/2):
                if pointer1.val>pointer2.val:
                    self.swap(pointer1,pointer2)
                pointer1=pointer2.next
                pointer2=pointer1.next
                
        
        
            
            
            
        
         
# @lc code=end

