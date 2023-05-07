#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    
    indices = []
    maxLength = -float("inf")
    
    def isPalindrome(self,low,high,s):
            
        while low>=0 and high<len(s) and s[low]==s[high]:
            low-=1
            high+=1

        if self.maxLength<high-low+1:
            self.maxLength = high-low+1
            self.indices = [low,high]
    
    def longestPalindrome(self, s: str) -> str:
        self.indices = []
        self.maxLength = -float("inf")
        
        if len(s) == 1:
            return s

        for i in range(len(s)):
            self.isPalindrome(i,i,s)
            
            self.isPalindrome(i,i+1,s)

        if self.indices:
            return s[self.indices[0]+1 : self.indices[1]]
        else:
            return ""

# @lc code=end

