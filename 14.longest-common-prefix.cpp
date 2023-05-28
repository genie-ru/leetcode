/*
 * @lc app=leetcode id=14 lang=cpp
 *
 * [14] Longest Common Prefix
 */

// @lc code=start
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string prefix = "";
        
        if (strs.size() == 0) {
            return prefix;
        }
        
        for (int i = 0; i < strs[0].length(); i++) {
            char c = strs[0][i];
            
            for (int j = 1; j < strs.size(); j++) {
                if (i >= strs[j].length() || strs[j][i] != c) {
                    return prefix;
                }
            }
            
            prefix += c;
        }
        
        return prefix;
    }
};
// @lc code=end

