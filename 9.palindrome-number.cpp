/*
 * @lc app=leetcode id=9 lang=cpp
 *
 * [9] Palindrome Number
 */

// @lc code=start
#include <iostream>
#include <string>
using namespace std;
class Solution {
public:
    bool isPalindrome(int x) {
        string x_str = to_string(x);
    string reversed_str = string(x_str.rbegin(), x_str.rend());
    if (x_str == reversed_str) {
        return true;
    } else {
        return false;
    }
    }
};
// @lc code=end

