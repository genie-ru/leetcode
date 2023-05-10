#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
    
        rows = [''] * numRows
        direction = -1
        row = 0
    
        for c in s:
            rows[row] += c
            if row == 0 or row == numRows - 1:
                direction *= -1
            row += direction
    
        return ''.join(rows)
# @lc code=end

