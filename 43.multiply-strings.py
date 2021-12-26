#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#

# @lc code=start
class Solution:
    
    def edgecases(self,num1,num2):
        if num1=="0" or num2=="0":
            return "0"
        
        
        return False

    def multiply(self, num1: str, num2: str) -> str:
        
        if self.edgecases(num1,num2):
            return self.edgecases(num1,num2)
        
        
        result=""
        
        add=0
        
        # set len(num2)<len(num1)
        
        if len(num2)>len(num1):
            temp=num1
            num1=num2
            num2=temp
        
        # 2 * 3
        # i=0 0th digit:=[0]*[0]
        
        # 123*456
        # i max = 4 digit = 2*2
        
        #  114514 * 23
        #  digit=5*1 i max=6 i min 
        
        
        for i in range(0,len(num1)+len(num2)-1):
            temp=add
            for j in range(max(0,i-len(num1)+1),min(len(num2),i+1)):
                
                # i-j < len(num1)
                # j>i-len(num1)
                
                temp+=int(num2[-1-j])*int(num1[-1-(i-j)])
            result=str(temp%10)+result
            add=int(temp/10)
        if add!=0:
            result=str(add)+result
        
        
        
        return result
        
# @lc code=end



num1="123"
num2="456"
a=Solution()
a.multiply(num1,num2)
