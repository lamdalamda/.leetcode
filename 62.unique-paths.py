#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def __init__(self):
        self.calculateddict={(1,1):1}
        #self.templist=[]
    def compare2(self,m,n):
        if m>=n:
            return (m,n)
        return (n,m)
    
    def uniquePaths_forward(self, m,n):
        if m<n:
            m,n=(n,m)
        
        
        if n==1:
            return 1
        if n==2: 

            return m
        
        templist=[]
        for i in range(m,0,-1):
            templist.append(i)
        
        for i in range(0,n-2):
            for j in range(m-2,-1,-1):
                templist[j]=templist[j]+templist[j+1]
            
        return templist[0]

        """
        7*3
        
        
                    1
                    1 
        1 1 1 1 1 1 1

                    1
        7 6 5 4 3 2 1 
        1 1 1 1 1 1 1

7*4

                  3->1
                  |  
        7 6 5 4 3 2 1 
        1 1 1 1 1 1 1
        
        """
    

    def uniquePaths_recursive_hash(self, m: int, n: int) -> int:
        if m*n==0: 
            raise ValueError
        if m==1: return 1
        if n==1: return 1
        # set m>n
        
        if m<n:
            m,n=(n,m)
        
        if (m,n) not in self.calculateddict:

            if m==n:
                if (m,n-1) not in self.calculateddict:
                    self.calculateddict[(m,n-1)]=self.uniquePaths_recursive_hash(m,n-1)
                self.calculateddict[(m,n)]=2*self.calculateddict[(m,n-1)]            
            else:
                if (m-1,n) not in self.calculateddict:
                    self.calculateddict[(m-1,n)]=self.uniquePaths_recursive_hash(m-1,n)
    
                
                if (m,n-1) not in self.calculateddict:
                    self.calculateddict[(m,n-1)]=self.uniquePaths_recursive_hash(m,n-1) 

                self.calculateddict[(m,n)]= self.calculateddict[(m,n-1)]+self.calculateddict[(m-1,n)]
        
        return self.calculateddict[(m,n)]        
        

    
    def uniquePaths(self, m: int, n: int):
        return self.uniquePaths_recursive_hash(m,n)
    
    def uniquePaths_recursive(self, m: int, n):
        if m*n==0: 
            raise ValueError
        if m==1: return 1
        if n==1: return 1
        
        return self.uniquePaths_recursive(m-1,n)+self.uniquePaths_recursive(m,n-1)
        # set m>n        
        
# @lc code=end

a=Solution()
a.uniquePaths(3,7)