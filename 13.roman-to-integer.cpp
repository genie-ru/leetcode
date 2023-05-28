/*
 * @lc app=leetcode id=13 lang=cpp
 *
 * [13] Roman to Integer
 */

// @lc code=start
#include <iostream>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char, int> roman_values = {
            {'I', 1}, {'V', 5}, {'X', 10}, {'L', 50}, {'C', 100}, {'D', 500}, {'M', 1000}
        };
        
        unordered_map<string, int> special_cases = {
            {"IV", 4}, {"IX", 9}, {"XL", 40}, {"XC", 90}, {"CD", 400}, {"CM", 900}
        };
        
        int num = 0;
        int i = 0;
        
        while (i < s.length()) {
            if (i < s.length() - 1 && special_cases.find(s.substr(i, 2)) != special_cases.end()) {
                num += special_cases[s.substr(i, 2)];
                i += 2;
            } else {
                num += roman_values[s[i]];
                i += 1;
            }
        }
        
        return num;
    }
};
// @lc code=end

