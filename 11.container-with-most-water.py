#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        
        while left < right:
            # 現在の面積を計算する
            area = min(height[left], height[right]) * (right - left)
            
            # 必要に応じてmax_areaを更新する
            max_area = max(max_area, area)
            
            # より小さい高さを持つポインタを移動する
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area

# @lc code=end

