/*
 * @lc app=leetcode id=16 lang=cpp
 *
 * [16] 3Sum Closest
 */

// @lc code=start
#include <vector>
#include <algorithm>
#include <cmath>

class Solution {
public:
    int threeSumClosest(std::vector<int>& nums, int target) {
        std::sort(nums.begin(), nums.end());
        return KSumClosest(nums, 3, target);
    }

private:
    int KSumClosest(std::vector<int> nums, int k, int target) {
        int N = nums.size();
        if (N == k) {
            int sum = 0;
            for (int i = 0; i < k; i++) {
                sum += nums[i];
            }
            return sum;
        }

        // target too small
        int current = 0;
        for (int i = 0; i < k; i++) {
            current += nums[i];
        }
        if (current >= target) {
            return current;
        }

        // target too big
        current = 0;
        for (int i = N - k; i < N; i++) {
            current += nums[i];
        }
        if (current <= target) {
            return current;
        }
        
        if (k == 1) {
            int closest = nums[0];
            int minDiff = std::abs(target - closest);
            for (int i = 1; i < N; i++) {
                int diff = std::abs(target - nums[i]);
                if (diff < minDiff) {
                    closest = nums[i];
                    minDiff = diff;
                }
            }
            return closest;
        }

        int closest = 0;
        for (int i = 0; i < k; i++) {
            closest += nums[i];
        }
        for (int i = 0; i < N - k + 1; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            int current = KSumClosest(std::vector<int>(nums.begin() + i + 1, nums.end()), k - 1, target - nums[i]) + nums[i];
            if (std::abs(target - current) < std::abs(target - closest)) {
                if (current == target) {
                    return target;
                } else {
                    closest = current;
                }
            }
        }

        return closest;
    }
};

// @lc code=end

// ヘッダーファイル <vector> と <algorithm> をインクルードしました。
// Python の List 型は、C++ では std::vector を使用します。
// Python の sum() 関数は、C++ ではループを使用して合計を計算しました。
// Python の abs() 関数は、C++ では std::abs() を使用しました。
// Python の enumerate() 関数は、C++ ではインデックスを使用してループしました。
// Python の key パラメーターを使用した min() 関数は、C++ では手動で最小値を追跡するループを使用しました。
// この C++ コードは、Python の Solution クラスの threeSumClosest メソッドと KSumClosest メソッドを再現します。ご参考までにご利用ください。