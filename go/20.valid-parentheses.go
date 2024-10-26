/*
 * @lc app=leetcode id=20 lang=golang
 *
 * [20] Valid Parentheses
 */

// @lc code=start
package main

func isValid(s string) bool {
    stack := []rune{}
    matchingBrackets := map[rune]rune{
        ')': '(', 
        '}': '{', 
        ']': '[',
    }

    for _, char := range s {
        // 開く括弧の場合はスタックに積む
        if char == '(' || char == '{' || char == '[' {
            stack = append(stack, char)
        } else {
            // 閉じる括弧がある場合
            if len(stack) == 0 {
                return false // スタックが空なら不正
            }
            top := stack[len(stack)-1] // スタックの最後の要素を取得
            stack = stack[:len(stack)-1] // スタックのトップを取り出す
            // 対応が正しいかチェック
            if matchingBrackets[char] != top {
                return false
            }
        }
    }
    return len(stack) == 0 // スタックが空なら全て正しく閉じられている
}

// @lc code=end
