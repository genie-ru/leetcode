/*
 * @lc app=leetcode id=5 lang=cpp
 *
 * [5] Longest Palindromic Substring
 */

// @lc code=start
#include <iostream>
#include <string>
#include <vector>
using namespace std;
class Solution {
public:
    string longestPalindrome(string s) {
        string t = "#";
        for (char c : s) {
            t += c;
            t += "#";
        }
        int n = t.size();
        vector<int> p(n);
        int c = 0, r = 0, max_len = 0, center = 0;
        for (int i = 0; i < n; ++i) {
            if (i < r) {
                p[i] = min(r - i, p[2 * c - i]);
            }
            while (i + p[i] + 1 < n && i - p[i] - 1 >= 0 && t[i + p[i] + 1] == t[i - p[i] - 1]) {
                ++p[i];
            }
            if (i + p[i] > r) {
                c = i;
                r = i + p[i];
            }
            if (p[i] > max_len) {
                max_len = p[i];
                center = i;
            }
        }
        return s.substr((center - max_len) / 2, max_len);
    }
};

// @lc code=end

