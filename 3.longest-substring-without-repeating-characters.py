#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        #brutal
        lenth=0
        for i in range(0,len(s)):
            strlist=[]
            for j in range(i,len(s)):

                if s[j] not in strlist:
                    strlist.append(s[j])
                else:
                    break
            if len(strlist)>lenth:
                lenth=len(strlist)
        return lenth        
        
        
        
# @lc code=end

        """
        #brutal
        lenth=0
        for i in range(0,len(s)):
            strlist=[]
            for j in range(i,len(s)):

                if s[j] not in strlist:
                    strlist.append(s[j])
                else:
                    break
            if len(strlist)>lenth:
                lenth=len(strlist)
        return lenth        
        
        
        """