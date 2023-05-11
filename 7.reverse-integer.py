#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x:int) -> int:
        reverse = 0
        sign = 1 if x > 0 else -1
        x *= sign
        while x>0:
            digit = x % 10
            reverse = reverse * 10 + digit
            x //= 10
        reverse*=sign
        return reverse if reverse >= -(2**31) and reverse <= (2**31 -1) else 0 
        
# @lc code=end

