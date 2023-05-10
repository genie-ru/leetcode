#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        result = ''
        n = len(s)
        cycleLen = 2 * numRows - 2
        for i in range(numRows):
            for j in range(0, n - i, cycleLen):
                result += s[j + i]
                if i != 0 and i != numRows - 1 and j + cycleLen - i < n:
                    result += s[j + cycleLen - i]
        return result
# @lc code=end

