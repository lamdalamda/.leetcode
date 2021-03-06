#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#
from typing import List
# @lc code=start



class Solution:
    def __init__(self):
        self.hashdict={}
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        return self.inner(sorted(candidates),target)

    def inner(self, candidates, target: int):
        index=0
        combinations=[]
        while index<len(candidates):

            if candidates[index]<target:
                for j in self.inner(candidates[index+1:],target-candidates[index]):
                    combinations.append(j+[candidates[index]])
                
            if candidates[index]==target:
                combinations.append([candidates[index]])
        
            if candidates[index]>target:
                break
                
            index+=1
            
            while index<len(candidates) and candidates[index]==candidates[index-1]:
                index+=1
                
        return combinations   
        
        
        
        
# @lc code=end

if __name__=="__main__":
    
    a=Solution()

    a.combinationSum2([10,1,2,7,6,1,5],8)