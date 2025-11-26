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

#### 2nd Submission ([code](./01_best_time_to_buy_and_sell_stock_02.py)) :

- Language: Python
- Memory: 52 MB (leetcode: 27.21 MB, beats 8.68%)
- Runtime: 0.883 seconds (leetcode: 143 ms, beats 11.54%)

讀了 NeetCode 的 hint 後嘗試寫的 solution，time O(n)，memory O(n)。
先求每一時刻賣出時的最低買入價格(即向左的最小值，可由左向右掃時存入 min_buy List, O(n))，再對每一時刻計算獲利量，更新 max_profit。

#### 3rd Submission ([code](./01_best_time_to_buy_and_sell_stock_03.py)) :

- Language: Python
- Memory: 52.3 MB (leetcode: 27.01 MB, beats 8.68%)
- Runtime: 0.86 seconds (leetcode: 150 ms, beats 7.08%)

寫 2nd submission 的 note 時突然想到，其實不用另存 min_buy List，可以直接算，重寫了 3rd 的 solution，  
time O(n), memory O(1)，但在效能上好像沒有明顯變化  
類似 NeetCode 提供的 Dynamic Programming 解法

#### 4th Submission ([code](./01_best_time_to_buy_and_sell_stock_04.py)) :

- Language: Python
- Memory: 52 MB (leetcode: 26.89 MB, beats 77.54%)
- Runtime: 0.799 seconds (leetcode: 127 ms, beats 29.54%)

讀了 NeetCode 的 two pointers 的解說後重寫。  
time O(n), memory O(1)。
想法是將左點設定為 buy，右點設定為 sell，右點一直往右移一格，計算 profit 並更新最大值  
當右點的值<左點時，表示找到了更佳的買入點，將左點的 index 更新為更佳的買入點
