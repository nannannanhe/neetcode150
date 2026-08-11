## (01) Valid Parentheses

### Problem

- neetcode: https://neetcode.io/problems/validate-parentheses/question
- leetcode(20): https://leetcode.com/problems/valid-parentheses/description/

### Time / Memory / Notes

#### First Submission ([code](./01_valid_parenthese_01.py)) :

- Language: Python
- Memory: 7.7 MB (leetcode: 19.30 MB Beats 23.97%)
- Runtime: 27 ms (leetcode: 3ms Beats 32.08%)

先用HashMap(dict)定義各括號的open/close，並以array實作stack。
順著string由前往後掃，如果是open就放進stack，是close就對照stack裡的最後一個元素是否為對應的open，是的話pop()，否則return False。

#### 2nd Submission ([code](./01_valid_parenthese_02.py)) :

- Language: Python
- Memory: 7.7 MB (leetcode: 19.37 MB Beats 23.97%)
- Runtime: 26 ms (leetcode: 0ms Beats 100%)

看了NeetCode的解析，其實想法和我第一次寫時是一樣的，但我沒有注意到題目裡定義input的字串s只會有括號組成，不會有其他字元，因此不需要判斷會有其他字元時的情況，
以及想檢查是否in dict.keys()時，只要寫in dict就好，重寫成比較pythonic的版本。

## (02) Min Stack

### Problem

- neetcode: https://neetcode.io/problems/minimum-stack/question
- leetcode(155): https://leetcode.com/problems/min-stack/description/

### Time / Memory / Notes

#### First Submission ([code](./02_min_stack_01.py)) :

- Language: Python
- Memory: 11.7 MB (leetcode: 30.99 MB Beats 97.22%)
- Runtime: 98 ms (leetcode: 100ms Beats 50.17%)

其實一開始`getMin`我是寫成`min(self.stack)`，但TLE，
查了確認python的min()的time complexity是O(n)，不符合題目規定的O(1)。
因此另建一個記錄min值的stack，當新push入的值，小於或等於目前的最小值時，push到min值stack的最尾(為考慮pop時的順序，等於也要push入記錄min值的stack)。
