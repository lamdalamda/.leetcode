#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head
        pointer1=head
        pointer2=head.next
        temp=pointer2.next
        pointer1.next=temp
        pointer2.next=pointer1
        head=pointer2
        
        pointer0=pointer1
        while pointer1.next is not None:
            #return (pointer1)
            pointer1=pointer1.next
            pointer2=pointer1.next
            if pointer2 is not None:
                temp=pointer2.next
                pointer1.next=temp
                pointer2.next=pointer1
                pointer0.next=pointer2
                
                pointer0=pointer1
            else:
                return head
        return head
# @lc code=end

