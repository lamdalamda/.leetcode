#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #edge case
        if target<=nums[0]:
            return 0
        if target>=nums[-1]:
            return len(nums)-1

        if len(nums)<6:
            for i in range(0,len(nums)-1):
                if nums[i]==target:
                    return i
                if nums[i]<target and nums[i+1]>target:
                    return i
        
        index1=0
        index2=len(nums)-1
        while index1<index2-4:
            
            middle=int((index1+index2)/2)
            if nums[middle]==target:
                return middle
            if nums[middle]<target:
                if nums[middle+1]>target:
                    return middle
                index1=middle
            else:
                index2=middle
                
        for i in range(index1,index2):
            if nums[i]==target:
                return i
            if nums[i]<target and nums[i+1]>target:
                return i
        if nums[index2]==target:
            return index2
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        vertical=[]
        for i in range(0,len(matrix)):
            vertical.append(matrix[i][0])
        tmp=self.searchInsert(vertical,target)
        
        tmp2=self.searchInsert(matrix[tmp],target)
        
        if matrix[tmp][tmp2]==target:
            return True
        return False
        
# @lc code=end

