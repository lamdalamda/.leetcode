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
        return self.mergeKLists_smarter(lists)
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
        if len(lists)==0:
            return None
        if len(lists)==1:
            if lists[0]==None: 
                return None
            else:
                return lists[0]
        
        else:
            return False
    
    def connect(self, lists: List[Optional[ListNode]],index1,pointer):
        
        """
        pointer
        |
        1   4
        | / |
        |/  |
        3    5 
        |
        |
        index1
        
        """
        pointer.next=lists[index1]
        lists[index1]=lists[index1].next
        pointer=pointer.next
        
        
        pass
        
    def merge_sort(self,list_to_sort):
        
        if len(list_to_sort)<=6:
            return sorted(list_to_sort)
        
        part1=self.merge_sort(list_to_sort[0:int(len(list_to_sort)/2)])
        part2=self.merge_sort(list_to_sort[int(len(list_to_sort)/2):])
        
        resultlist=[]
        
        while len(part1)>0 or len(part2)>0:
            if len(part1)==0:
                resultlist.extend(part2)
            if len(part2)==0:
                resultlist.extend(part1)
            
            if part1[0]<part2[0]:
                resultlist.append(part1.pop(0))
            else:
                resultlist.append(part2.pop(0))
        
        
        
    def initial_compare(self,lists):
        initial_compare_dict={}
        for i in range(0,len(lists)):
            #if lists[i]==None:
                #initial_compare_dict[None].append(i)
            #else:
            
            if lists[i] !=None:
                if lists[i].val in initial_compare_dict:
                    initial_compare_dict[lists[i].val].append(i)
                else:
                    initial_compare_dict[lists[i].val]=[i]
        
        return initial_compare_dict
        

        
        
    
    def mergeKLists_smarter(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:        
        if self.edge_cases(lists) != False:
            return self.edge_cases(lists)        
        
        root=ListNode()
        pointer=root
        
        value_dict=self.initial_compare(lists)
        
        while len(value_dict) > 0:
            
            minval=min(value_dict.keys())
            
            index=value_dict[minval].pop()
            
            
            # connect the pointer to the listnode with minval, with index=index
            pointer.next=lists[index]
            lists[index]=lists[index].next
            pointer=pointer.next    
            
            # add the next value to the value_dict
            if lists[index]!= None:
                if lists[index].val in value_dict:
                    value_dict[lists[index].val].append(index)
                else:
                    value_dict[lists[index].val]=[index]
                
            # detect after pop the minval, the dictionary is empty
        
            if len(value_dict[minval])==0:
                value_dict.pop(minval)
                
                   

            
        
        return root.next
        
        
        
        
# @lc code=end

