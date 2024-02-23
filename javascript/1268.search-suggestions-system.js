/*
 * @lc app=leetcode id=1268 lang=javascript
 *
 * [1268] Search Suggestions System
 */

// @lc code=start
/**
 * @param {string[]} products
 * @param {string} searchWord
 * @return {string[][]}
 */
var suggestedProducts = function(products, searchWord) {
    products.sort()
    let arr=[]
    for(let i = 0; i<searchWord.length;i++){
        let search = searchWord.slice(0,i+1) 
           let tem = products.filter(val=> val.slice(0,i+1) === search )
            arr.push(tem.slice(0,3))
          }
    return arr
};
// @lc code=end

