/*
 * @lc app=leetcode id=10 lang=cpp
 *
 * [10] Regular Expression Matching
 */

// @lc code=start
#include <vector>
using namespace std;

class Solution {
public:
    bool isMatch(string s, string p) {
        // dp[i][j] は s の最初の i 文字と p の最初の j 文字がマッチするかどうかを表すフラグ
        vector<vector<bool>> dp(s.length() + 1, vector<bool>(p.length() + 1, false));

        // 空文字列同士は常にマッチする
        dp[0][0] = true;

        // パターンの先頭が '*' である場合の初期化
        for (int j = 1; j <= p.length(); j++) {
            if (p[j - 1] == '*') {
                dp[0][j] = dp[0][j - 2];
            }
        }

        // 動的計画法によるマッチング判定
        for (int i = 1; i <= s.length(); i++) {
            for (int j = 1; j <= p.length(); j++) {
                if (s[i - 1] == p[j - 1] || p[j - 1] == '.') {
                    dp[i][j] = dp[i - 1][j - 1];
                }
                else if (p[j - 1] == '*') {
                    if (s[i - 1] == p[j - 2] || p[j - 2] == '.') {
                        dp[i][j] = dp[i][j - 2] || dp[i - 1][j];
                    }
                    else {
                        dp[i][j] = dp[i][j - 2];
                    }
                }
            }
        }

        return dp[s.length()][p.length()];
    }
};

// @lc code=end

