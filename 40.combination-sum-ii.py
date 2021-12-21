#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def __init__(self):
        self.hashdict={}
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results=[]
        self.inner(sorted(candidates),target,[],results)
        return results
    def inner(self, candidates: List[int], target: int,paths,results) -> List[List[int]]:

        if target<0:
            return
        if target==0:
            paths.append([])

        
        for i in range(0,len(candidates)):
            tmp=candidates
            minus=tmp.pop(i)
            self.inner(tmp,target-minus,paths,results)
        

            
        
                
# @lc code=end

