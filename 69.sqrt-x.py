#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        if x==1:
            return 1
        jump=x
        
        root=0
        while jump>1:
            jump=int(jump/2+0.5)
            tempr=(root+jump)**2
            if tempr==x:
                return root+jump
            if tempr<x:
                root+=jump
        return root
            
# @lc code=end

