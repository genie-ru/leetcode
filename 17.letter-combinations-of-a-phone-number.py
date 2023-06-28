#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:
#         if not digits:
#             return []
        
#         phone = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
#         res = []
        
#         def backtrack(combination, next_digits):
#             if not next_digits:
#                 res.append(combination)
#                 return
            
#             for letter in phone[next_digits[0]]:
#                 backtrack(combination + letter, next_digits[1:])
        
#         backtrack("", digits)
#         return res
class Solution:
    def __init__(self):
        self.phone = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        self.result = []

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        self.backtrack("", digits)
        return self.result
    
    def backtrack(self, combination, next_digits):
        if not next_digits:
            self.result.append(combination)
            return
        
        for letter in self.phone[next_digits[0]]:
            self.backtrack(combination + letter, next_digits[1:])
# @lc code=end

