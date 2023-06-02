/*
 * @lc app=leetcode id=15 lang=cpp
 *
 * [15] 3Sum
 */

// @lc code=start
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> ans;
        sort(nums.begin(), nums.end());
        for(int i = 0; i < nums.size(); i++){
            int a = nums[i];
            if(i != 0 and a == nums[i-1]) continue;
            int l = i+1, r = nums.size()-1;

            while(l < r){
                int threeSum = a + nums[l] + nums[r];
                if(threeSum == 0)
                {
                    ans.push_back({a, nums[l], nums[r]});
                    l += 1;
                    while( l < r && nums[l] == nums[l-1])
                    l+=1;
                }
                else if(threeSum > 0) r-=1;
                else l+=1;
            }
        }
        return ans;
    }
};
// @lc code=end

