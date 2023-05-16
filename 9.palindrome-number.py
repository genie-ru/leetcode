#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        reversed_str = x_str[::-1]
        if x_str == reversed_str:
            return True
        else:
            return False
            
# @lc code=end

