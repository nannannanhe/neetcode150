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

## (02) Longest Substring Without Repeating Characters

### Problem

- neetcode: https://neetcode.io/problems/longest-substring-without-duplicates/question
- leetcode(3): https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

### Time / Memory / Notes

#### 1st Submission ([code](./02_longest_substring_without_repeating_characters_01.py)) :

- Language: Python
- Memory: 52.3 MB (leetcode: 17.82 MB, beats 52.41%)
- Runtime: 0.85 seconds (leetcode: 548 ms, beats 5.00%)

以為設兩個點就是 sliding window，讀了 NeetCode 的 solution 才發現我的寫法其實是 brute force...
time O(n\*m), memory O(m), m 為 unique 的元素個數
由左點為起點，右點向右移動，當右點的元素不重複，存入 word_set，而當右點的元素已在 word_set 裡時，重置 word_set，將左點向右一格，右點重置為左點加一，重新查找

#### 2nd Submission ([code](./02_longest_substring_without_repeating_characters_02.py)) :

- Language: Python
- Memory: 52.3 MB (leetcode: 18.08 MB, beats 11.97%)
- Runtime: 0.806 seconds (leetcode: 23 ms, beats 30.72%)

真正的 sliding window，time O(n), memory O(m)  
當右點遇到已在 set 裡的元素時，重複 remove 掉左點的元素，將左點向右一格，重複直至右點不在 set 裡，  
之後將右點元素加入 set，更新長度，並持續向右一格

#### 3rd Submission ([code](./02_longest_substring_without_repeating_characters_03.py)) :

- Language: Python
- Memory: 52.4 MB (leetcode: 17.69 MB, beats 96.66%)
- Runtime: 0.775 seconds (leetcode: 23 ms, beats 30.72%)

optimal 的寫法，  
不用 while 去調整左點的位置，而是利用 dict 記錄該元素最後出現的 index，  
在右點出現重複的元素時，調整左點至 max(左點目前的位置，該元素最後出現的位置+1)
計算長度時不使用 dict 的元素量，而是用目前的左點和右點來計算
調整左點那步有點 tricky，我本來想說把左點調到該元素最後出現的位置就好了吧，但在 abba 時會出錯(因為左點會跑到更前的地方，導致中間的調整被蓋過，會有重複元素)

## (03) Longest Repeating Character Replacement

### Problem

- neetcode: https://neetcode.io/problems/longest-repeating-substring-with-replacement/question
- leetcode(424): https://leetcode.com/problems/longest-repeating-character-replacement/description/

### Time / Memory / Notes

#### 1st Submission ([code](./03_longest_repeating_character_replacement_01.py)) :

- Language: Python
- Memory: 53 MB (leetcode: LTE on 36th testcase)
- Runtime: 0.807 seconds (leetcode: LTE on 36th testcase)

看了解說才寫出來，但可能因為每個 iteration 都用了 Counter 來算出現次數最多的字元，leetcode 會 LTE。
