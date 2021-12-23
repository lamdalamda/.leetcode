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
        results=self.inner(sorted(candidates),target)
        return results
    def inner(self, candidates: List[int], target: int) -> List[List[int]]:
        
        #sorted candidates:
        # only return target
        # results containing path to this target
        
        # 1 1 2 5 6 7 8 target =8
        combinations=[]
        # 1 2 5 6 7 10 target = 7 results=1
        for i in range(0,len(candidates)-1):
            if target>candidates[i]:
                tmp=self.inner(candidates[i+1:],target-candidates[i])
                if len(tmp)>0:
                    for j in tmp:
                        combinations.append(j+[candidates[i]])
                    pass 

            if target==candidates[i]:
                combinations.append([candidates[i]])
                

            
            if target<candidates[i]:
                break 
        if target==candidates[-1]:
            combinations.append([candidates[-1]])

        return combinations
     
        
if __name__=="__main__":
    
    a=Solution()
    a.combinationSum2([10,1,2,7,6,1,5],8)
            
        
                
# @lc code=end

