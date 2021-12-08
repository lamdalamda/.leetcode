#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        indexdict={}
        for i in nums:
            indexdict[i] =1
        smallest=1
        while True:
            if smallest not in indexdict:
                return smallest
            else:
                smallest+=1
            
# @lc code=end

