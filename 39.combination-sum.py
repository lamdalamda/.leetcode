#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def __init__(self):
        self.resultdict={}
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        self.resultdict[min(candidates)]=[[min(candidates)]]
        
        return self.combinationSum2(sorted(candidates),target)
        
    """
    assume: candidate = 1,2,4
    
    target =9
    
    result = 441 4221 411111 22221 222111 2211111 21111111 111111111
    
    (return 4-5 2-7 )
    
    """

        
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        if min(candidates)>target:
            # 2,3,45, target=1
            return None
        
        if target in self.resultdict:
            return self.resultdict[target]
        
        thisresult=[]
        
        if target in candidates:
            thisresult.append([target])
        
        for i in candidates:
            tmp=self.combinationSum(candidates,target-i)
            
            if (tmp is not None):
                for j in tmp:
                    if j[0]<=i:
                        thisresult.append([i]+j)
                        
        self.resultdict[target]=thisresult
        return thisresult        
        


        
        
        
# @lc code=end

