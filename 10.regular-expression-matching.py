#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # dp[i][j] は s の最初の i 文字と p の最初の j 文字がマッチするかどうかを表すフラグ
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

        # 空文字列同士は常にマッチする
        dp[0][0] = True

        # パターンの先頭が '*' である場合の初期化
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        # 動的計画法によるマッチング判定
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    if s[i - 1] == p[j - 2] or p[j - 2] == '.':
                        dp[i][j] = dp[i][j - 2] or dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i][j - 2]
        
        return dp[len(s)][len(p)]



# @lc code=end

