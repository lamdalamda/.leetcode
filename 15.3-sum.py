#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def special_case(self,nums):
        count=0
        for i in nums:
            if i==0:
                count+=1
        if len(nums)<3:
            return 1
        if min(nums)>0:
            return 1
        if max(nums)<0:
            return 1
        if count>2:
            return 0
        return 2
        
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        resultlist=[]
        special=self.special_case(nums)
        if special==1:
            return []
        if special==0:
            resultlist.append([0,0,0])
        positive_nums=[]
        negative_nums=[]
        positive_combinations={}
        negative_combinations={}
        listlenth=len(nums)
        for i in range(0,listlenth):
            if nums[i]>=0:
                positive_nums.append(nums[i])
                negative_combinations[-nums[i]]=[]
            else:
                negative_nums.append(nums[i])
                positive_combinations[-nums[i]]=[]

        for i in range(0,len((positive_nums))):
            for j in range(i+1,len(positive_nums)):
                sum=positive_nums[i]+positive_nums[j]
                if sum in positive_combinations:
                    if positive_nums[i] not in positive_combinations[sum]:
                        positive_combinations[sum].append(positive_nums[i])
                        positive_combinations[sum].append(positive_nums[j])
                        resultlist.append([-sum,positive_nums[i],positive_nums[j]])
        for i in range(0,len((negative_nums))):
            for j in range(i+1,len(negative_nums)):
                sum=negative_nums[i]+negative_nums[j]
                if sum in negative_combinations:
                    if negative_nums[i] not in negative_combinations[sum]:
                        negative_combinations[sum].append(negative_nums[i])
                        negative_combinations[sum].append(negative_nums[j])
                        resultlist.append([-sum,negative_nums[i],negative_nums[j]])
        return resultlist
            
                
        
# @lc code=end

