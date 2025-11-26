## (01) Best Time to Buy and Sell Stock

### Problem

- neetcode: https://neetcode.io/problems/buy-and-sell-crypto/question
- leetcode(121): https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

### Time / Memory / Notes

#### First Submission ([code](./01_best_time_to_buy_and_sell_stock_01.py)) :

- Language: Python
- Memory: 52 MB (leetcode: TLE on 199th testcase)
- Runtime: 0.874 seconds (leetcode: TLE on 199th testcase)

Brute Force，O(n^2)。  
對每一天買入，算之後的每一天賣出時的獲利，找最大值。
嘗試用當不獲利(即賣出<買入)時 skip 來減少計算量，但似乎沒有太大幫助
