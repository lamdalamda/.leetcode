#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        reflist=[]
        lenth=0
        newlist=[]
        for i in range(0, len(s)):
            if s[i] not in newlist:
                newlist.append(s[i])
            else:
                if len(newlist)>len(reflist):
                    reflist=newlist

                newlist=[]
                newlist.append(s[i])
        return max(len(newlist),len(reflist))
        
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