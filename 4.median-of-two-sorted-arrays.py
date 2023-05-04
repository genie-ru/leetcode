#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
from typing import List, Tuple

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        i_min, i_max, half_len = 0, m, (m + n + 1) // 2
        
        while i_min <= i_max:
            i = (i_min + i_max) // 2
            j = half_len - i
            
            if i < m and nums2[j-1] > nums1[i]:
                # i is too small, adjust the lower bound
                i_min = i + 1
            elif i > 0 and nums1[i-1] > nums2[j]:
                # i is too big, adjust the upper bound
                i_max = i - 1
            else:
                # i is perfect
                if i == 0: max_of_left = nums2[j-1]
                elif j == 0: max_of_left = nums1[i-1]
                else: max_of_left = max(nums1[i-1], nums2[j-1])
                
                if (m + n) % 2 == 1:
                    return max_of_left
                
                if i == m: min_of_right = nums2[j]
                elif j == n: min_of_right = nums1[i]
                else: min_of_right = min(nums1[i], nums2[j])
                
                return (max_of_left + min_of_right) / 2

        
# @lc code=end

