#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        strx=str(x)
        for i in range(0,int(0.5*len(strx))):
            if strx[i]!=strx[len(strx)-i-1]:
                return False
        
        return True
        
# @lc code=end

