#
# @lc app=leetcode id=1268 lang=python3
#
# [1268] Search Suggestions System
#

# @lc code=start
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        list_ = []
        products.sort()
        for i, c in enumerate(searchWord):
            products = [ p for p in products if len(p) > i and p[i] == c ]
            list_.append(products[:3])
        return list_
# @lc code=end

