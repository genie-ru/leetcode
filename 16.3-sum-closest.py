#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        return self.KSumClosest(nums, 3, target)

    def KSumClosest(self, nums: List[int], k: int, target: int) -> int:
        N = len(nums)
        if N == k:
            return sum(nums[:k])

        # targetが小さすぎる場合
        current = sum(nums[:k])
        if current >= target:
            return current

        # targetが大きすぎる場合
        current = sum(nums[-k:])
        if current <= target:
            return current
        
        if k == 1:
            return min([(x, abs(target - x)) for x in nums], key=lambda x: x[1])[0]

        closest = sum(nums[:k])
        for i, x in enumerate(nums[:-k+1]):
            if i > 0 and x == nums[i-1]:
                continue
            current = self.KSumClosest(nums[i+1:], k-1, target - x) + x
            if abs(target - current) < abs(target - closest):
                if current == target:
                    return target
                else:
                    closest = current

        return closest
# このコードは、与えられた整数配列 nums と目標値 target に対して、最も近い合計を求めるためのアルゴリズムを提供します。アルゴリズムは、3つの整数の合計が目標値に最も近いものを見つけることを目指しています。

# まず、threeSumClosest メソッドは、与えられた整数配列を昇順にソートします。ソートされた配列を引数として、KSumClosest メソッドを呼び出して、3つの整数の合計に対して最も近い合計を求めます。

# KSumClosest メソッドでは、与えられた整数配列 nums、パラメータ k（合計の要素数）、目標値 target を受け取ります。最も近い合計を求めるために以下の手順を実行します：

# 配列 nums の要素数 N を取得します。
# N が k と等しい場合、nums の最初の k 個の要素の合計を返します。これは、すべての要素を合計に含める唯一の選択肢です。
# 目標値 target が小さすぎる場合、nums の最初の k 個の要素の合計を返します。これは、配列が既にソートされているため、最小の k 個の要素の合計が目標値に最も近い値となるからです。
# 目標値 target が大きすぎる場合、nums の最後の k 個の要素の合計を返します。これは、配列が既にソートされているため、最大の k 個の要素の合計が目標値に最も近い値となるからです。
# k が 1 の場合、nums の要素の中から目標値 target に最も近い値を見つけ、その値を返します。これは、3つの整数の合計ではなく、単一の整数の場合です。
# 上記の特殊なケースではない場合、最も近い合計を保持する変数 closest を初期化します。
# 配列 nums を順番に反復処理し、各要素 x に対して以下の処理を行います：
# インデックス i と要素 x を取得します。
# 以前の要素と重複している場合は、スキップして次の要素に進みます。
# 要素 x を目標値から引いた残りの合計を再帰的に求めます。これにより、残りの k-1 個の要素の合計を計算することができます。
# 求めた残りの合計に要素 x を足して、現在の合計を得ます。
# 現在の合計と目標値 target との絶対値の差が、最も近い合計と目標値 target との絶対値の差よりも小さい場合、最も近い合計を更新します。
# もし現在の合計が目標値と完全に一致する場合は、目標値の合計を返します。
# それ以外の場合は、最も近い合計を保持したまま反復処理を続けます。
# 反復処理が終了したら、最も近い合計を返します。
# このアルゴリズムは、配列をソートしているため、要素の組み合わせを効率的にチェックし、最も近い合計を見つけることができます。
# @lc code=end

