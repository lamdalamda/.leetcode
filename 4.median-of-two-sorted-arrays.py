#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return self.on(nums1,nums2)
        
    def edgecases(self, nums1: List[int], nums2: List[int]) -> float:
        if nums1[-1]<=nums2[0]: 
            if len(nums1)==len(nums2): 
                return (nums1[-1]+nums2[0])/2
            if (len(nums1)+len(nums2))%2==1:
                # 1 2 
                # 3 4 5 6 
                if len(nums1)<len(nums2):      
                    return nums2[int((len(nums2)-len(nums1))/2)]
                else:
                    return nums1[int((len(nums1)-len(nums2))/2)]
            else:
                if len(nums1)<len(nums2):      
                    return (nums2[int((len(nums2)-len(nums1))/2)]+nums2[int((len(nums2)-len(nums1))/2)-1])/2
                else:
                    return (nums1[int((len(nums1)-len(nums2))/2)]+nums1[int((len(nums1)-len(nums2))/2)-1])/2      
        return False          
    def findMedianSortedArrays1(self, nums1: List[int], nums2: List[int]) -> float:
        if self.edgecases(nums1,nums2)!=False:
            return self.edgecases(nums1,nums2)

        
        

# @lc code=end

