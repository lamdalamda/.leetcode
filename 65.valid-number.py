#
# @lc app=leetcode id=65 lang=python3
#
# [65] Valid Number
#

# @lc code=start
class Solution:
    def __init__(self):
        self.digitdict={}
        self.interger="1234567890"
        self.specialchar="eE.+-"
    # format
    # +/- *** . *** e/E +/-  *** 
        
        
    def isNumber(self, s: str) -> bool:
        negative_positive_at_front=False
        decimal_dot=False
        eorE=False
        negative_positive_after_e=False
        i=0
        if s==".":return False
        if s[0] in "+-":
            negative_positive_at_front=True
            i=1
        if s[0] in "eE":
            return False
        while i<len(s):
            if s[i] in "eE":
                if eorE or i==len(s)-1:
                    return False
                else:
                    eorE=True
                    if i<len(s)-1:
                        if s[i+1] in "+-":
                            i+=1
                    
            if s[i] in "+-":
                return False
            
            if s[i] == ".":
                if eorE or decimal_dot:
                    return False
                decimal_dot=True
            
            
            i+=1
        pass
        return True
    
    
    
# @lc code=end

