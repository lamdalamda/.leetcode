#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def compare(self, list1,list2):
        if list1 ==None:
            if list2 ==None:
                return (None,list1,list2)
            else:
                return (list2.val,list1,list2.next)
        if list2==None:
            return (list1.val,list1.next,list2)
        if list1.val<list2.val:
            return (list1.val,list1.next,list2)
        return(list2.val,list1,list2.next)

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        rootnode=ListNode()
        thisnode=rootnode

        if (list1==None and list2==None):
            return None
        while True:
            thisnode.val,list1,list2=self.compare(list1,list2)
            if (list1==None and list2==None):
                break
            thisnode.next=ListNode()
            thisnode=thisnode.next

        return rootnode
            

            
            
            
# @lc code=end

