#
# @lc app=leetcode id=60 lang=python3
#
# [60] Permutation Sequence
#

# @lc code=start
class Solution:
    def unique_permutations_num(self,n): 
        if n==1:
            return 1
        return n*self.unique_permutations_num(n-1)
    def getPermutation(self, n: int, k: int) -> str:
        """
        1234
        1243
        1324
        1342
        1423
        1432
        
        1~6
        
        """
        accelerator={0:1}
        numberpool=[]
        result=""
        for i in range(1,n+1):
            numberpool.append(str(i))
        for i in range(1,n):
            accelerator[i]=i*accelerator[i-1]
        # numberpool=[1,2,3,4]
        k=k-1
        for i in range(n-1,0,-1):
            result+=numberpool.pop(int(k/(accelerator[i])))
            k=k%(accelerator[i])
        
        result+=(numberpool.pop())
        return result


# @lc code=end

a=Solution()
print(a.unique_permutations_num(5))