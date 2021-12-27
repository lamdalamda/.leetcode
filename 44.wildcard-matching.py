#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#

# @lc code=start
class Solution:
    def edgecases(self,s,p):
        
        
    def isMatch(self, s: str, p: str) -> bool:
        
        if p[0]!="*":
            if s[0]==p[0] or p[0]=="?":
                return self.isMatch(s[1:],p[1:])
            else:
                return False
        
        
# ajdnoaihfgweio**a**d**gpumhgfoieuawhgiouaewhgioa


#  *d*f*?* =
#  *d*f*
        
        # *asf?ff*k?f*n*w*e*
        
        
# @lc code=end
