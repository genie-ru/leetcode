#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 辞書型の変数を定義し、文字とそのインデックスを保持する
        char_dict = {}
        # 結果の最大値と、現在の部分文字列の左端を保持する変数を初期化する
        max_len, left = 0, 0
        # 文字列を1文字ずつ処理するループ
        for right, char in enumerate(s):
            # もし文字が既出であれば、左端の位置を重複文字の次の位置に移動する
            if char in char_dict and char_dict[char] >= left:
                left = char_dict[char] + 1
            # 文字とそのインデックスを辞書に登録する
            char_dict[char] = right
            # 現在の部分文字列の長さを計算する
            max_len = max(max_len, right - left + 1)
        return max_len

# @lc code=end

