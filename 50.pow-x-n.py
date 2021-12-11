#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow1(self, x: float, n: int) -> float:
        if n==0:
            return 1
        if n<0:
            return 1/self.myPow(x, -n)
        if n==1:
            return x
        if n%2==1:
            temp=self.myPow(x, int(n/2))
            return temp*temp*x
        temp=self.myPow(x, int(n/2))
        return temp*temp
#304/304 cases passed (20 ms)
#Your runtime beats 99.3 % of python3 submissions
#Your memory usage beats 18.37 % of python3 submissions (14.4 MB)


    
    
    def myPow2(self, x: float, n: int) -> float:
        # time limit exceed!
        if n==0:
            return 1
        if n<0:
            return 1/self.myPow(x, -n)
        if n==1:
            return x
        if n%2==1:

            return self.myPow(x, int(n/2))*self.myPow(x, int(n/2))*x

        return self.myPow(x, int(n/2))*self.myPow(x, int(n/2))      
    
    def dectobin(self,dec=10):
        # 10 -> 8+2 -> 1010
        # 25 -> 16+8+1 -> 11001
        # 16 -> 10000
        
        # 25 -> bindict[16]=1, bindict[4]=0
        
        bindict={}
        digitlist=[]
        
        digit=1
        while dec>=1:
            bindict[digit]=dec%(2)
            dec=int(dec/2)
            digitlist.append(digit)
            digit=digit+1
        return bindict,digitlist
    
    
    #convert decimal to binary dictionary
    
    def myPow3(self, x: float, n: int) -> float:
        if n==0:
            return 1
        if n<0:
            return 1/self.myPow(x, -n)
        if n==1:
            return x  
        if n==2:
            return x*x
        resultdict={}
        resultdict[1]=x
        binary_dict,digitlist=self.dectobin(n)
        for i in digitlist[1:]:
            # 1,2,3,4,5
            # 1,2,4,8,16
            resultdict[i]=resultdict[i-1]*resultdict[i-1]
        result=1
        for i in binary_dict:
            if binary_dict[i]!=0:
                result=result*resultdict[i]
        return result
  
    def outerloop4(self,x:float,n:int,lastresult=1,lastpower=1024):
        if n>=1:
            newpower=lastpower*lastpower
            if n%2==1:
                return self.outerloop4(x,int(n/2),lastresult*lastpower,newpower)
            else:
                return self.outerloop4(x,int(n/2),lastresult,newpower)                
        else:
            return lastresult
        


    def myPow4(self, x: float, n: int) -> float:
        if n==0:
            return 1
        if n<0:
            return 1/self.myPow(x, -n)
        if n==1:
            return x  
        if n==2:
            return x*x
        
        return self.outerloop4(x,n,1,x)
        
#        Your runtime beats 66.03 % of python3 submissions
#Your memory usage beats 18.37 % of python3 submissions (14.5 MB)
        
        
        pass
    def myPow(self, x: float, n: int) -> float:
        return self.myPow(x, n)
# @lc code=end
a=Solution()
a.myPow3(2.0,10)
