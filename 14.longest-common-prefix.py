#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:            
    # if strs is empty, return empty string
        if not strs:
            return ""

        # if strs has only one element, return that element
        if len(strs) == 1:
            return strs[0]

        # find the shortest string in strs
        shortest = min(strs, key=len)

        # compare each character of shortest with each character of the other strings
        for i, char in enumerate(shortest):
            for other in strs:
                if other[i] != char:
                    return shortest[:i]

        return shortest
# @lc code=end

