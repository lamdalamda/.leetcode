#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def __init__(self):
        self.hashdict={}
    def determine(self,s="",length=0):
        if len(s)<length:
            return False
        for i in range(0,int(len(s)/2)):
            if s[i]!=s[len(s)-i-1]:
                return False
        return True
    def longestPalindrome_brutal(self, s: str) -> str:
        
        #brutal,time limit exceeded
        maxlength=0
        maxstring=""
        for i in range(0,len(s)):
            for j in range(i,len(s)):
                if self.determine(s[i:j+1],maxlength):
                    maxstring=s[i:j+1]
                    maxlength=j+1-i
                    
        return maxstring
    
    def get_longest_result(self,resultlist=[]):
        lenth=0
        longest_string=""
        for i in resultlist:
            if len(i)>lenth:
                lenth=len(i)
                longest_string=i
        return longest_string
            
               
    def longestPalindrome_dynamic(self, s: str) -> str:                    
        #dynamic ?
        if s in self.hashdict:
            return self.hashdict[s]
        if len(s)==1:
            self.hashdict[s]=s
            return s
        #a
        if len(s)==2:
            if s[0]==s[1]:
                self.hashdict[s]=s
                return s
        #aa
            else:
                self.hashdict[s]=s[0]
                return s[0]
        #ab
        
        #if >=3
        # suppose =3

        for i in range(0,int(len(s)/2)):
            # s=3, range(0,1).,s=4,range(0,2)
            if s[i]!=s[len(s)-i-1]:
            #if s[0]!s[3-0-1]
                s1=self.longestPalindrome(s[0:len(s)-1])
                s2=self.longestPalindrome(s[1:len(s)])
                if len(s1)>len(s2):
                    self.hashdict[s]=s1
                    return s1
                self.hashdict[s]=s2
                return s2
        self.hashdict[s]=s
        return s
        # slower than brutal
    

    def longestPalindrome_crystal(self, s: str) -> str:          
        
        treedict={}
        
        
    def longestPalindrome(self, s: str) -> str:     
        return self.longestPalindrome_brutal(s)
            
            
            
                         
# @lc code=end

        """
        len(s)=3:
            if len(s)==3:
                #aba
            if s[0]==s[2]:
                return s
            
            resultlist=[]
            resultlist.append(self.longestPalindrome(s[0:2]),self.longestPalindrome(s[1:3]))
            return self.get_longest_result(resultlist)
        """