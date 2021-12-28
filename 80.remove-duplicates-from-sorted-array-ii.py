#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<3:
            return len(nums)
        #nums>=3
        #checkingindex=1
        new_num_comparing_to_index=0
        thisnumber_count=True 
        # 1st appear: unknown->True. secondappear: True->False. 3rd appear:get the false status

        for checkingindex in range(1,len(nums)):
            
            if nums[checkingindex]==nums[new_num_comparing_to_index]:
                if thisnumber_count:
                    # this is the 2nd appearance
                    new_num_comparing_to_index+=1
                    thisnumber_count=False
                    nums[new_num_comparing_to_index]=nums[checkingindex]

            else:
                thisnumber_count=True
                new_num_comparing_to_index+=1
                nums[new_num_comparing_to_index]=nums[checkingindex]
                
        return new_num_comparing_to_index+1

# @lc code=end

