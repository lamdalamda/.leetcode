#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
        

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        #return self.threeSumClosest_brutal(nums,target)
        return self.threeSumClosest_improtve1(nums,target)

    def threeSumClosest_brutal(self, nums: List[int], target: int) -> int:
               
        if len(nums)<3:
            return []
        resultlist=[]

        indexdict={}
        listlenth=len(nums)
        smallest=(abs(nums[0]+nums[1]+nums[2]-target),nums[0],nums[1],nums[2])
        for i in range(0,listlenth):
            for j in range(i+1,listlenth):
                for k in range(j+1,listlenth):
                    this_dist=abs(nums[i]+nums[j]+nums[k]-target)
                    if this_dist<smallest[0]:
                        smallest=(this_dist,nums[i],nums[j],nums[k])

        return smallest[1]+smallest[2]+smallest[3]      

    def threeSumClosest_improtve1(self, nums: List[int], target: int) -> int:
        if len(nums)<3:
            return []

        indexdict={}
        listlenth=len(nums)

        resultdict={}
        
        
        for i in range(0,listlenth):
            for j in range(i+1,listlenth):
                indexdict[nums[i]+nums[j]]=[nums[i],nums[j]]
        
        for i in range(0,listlenth):
            resultdict[target-nums[i]]=nums[i]
        
        for distance in range(0,20000):
            for i in resultdict:
                if i+distance in indexdict:
                    return i+distance
                
       
                
# @lc code=end

