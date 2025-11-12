## (06) Encode and Decode Strings

### Problem

- neetcode: https://neetcode.io/problems/string-encode-and-decode?list=neetcode150
- leetcode(271): https://leetcode.com/problems/encode-and-decode-strings

### Time / Memory / Notes

#### First Submission ([code](./06_encode_and_decode_strings_01.py)) :

- Language: Python
- Memory: 52.3 MB
- Runtime: 0.798 seconds

單純以難以出現在一般 string 裡的文字為考量，使用'\u0001'為 encode 的分隔符號。 缺點:當要 encode 的 list 裡包含有'\u0001'時，會無法正確 decode。優點:實裝非常快

#### Second Sumission ([code](./06_encode_and_decode_strings_02.py)) :

- Language: Python
- Memory: 52.2 MB
- Runtime: 0.892 seconds

參考 NeetCode 的 solution 後重寫。  
思考方式為，encode 時，在每個 string 前加[長度][分隔符(可任意)]。在 decode 時，由於會先找出長度後，直接 slice 出該文字，因此即使文字中有使用分隔符，也不會影響 decode。

## (07) Products of Array Except Self

### Problem

- neetcode: https://neetcode.io/problems/products-of-array-discluding-self?list=neetcode150
- leetcode(238): https://leetcode.com/problems/product-of-array-except-self/description/

### Time / Memory / Notes

#### First Submission ([code](./07_products_of_array_except_self_01.py)) :

- Language: Python
- Memory: 52.3 MB (leetcode:23.04 MB, Beats 98.35%)
- Runtime: 0.743 seconds (leetcode:18ms, Beats 90.08%)

其實一開始直覺是用 Brute Force 真的一個一個乘，time 會是 O(n^2)，不過題目描述裡提到 Could you solve it in O(n)time without using the division operation?，才想到可以先開始就先把 total 的乘積算出來，再用除的。 關於 0 的個數的判斷沒有寫好，可以先判斷 zero_nums>1 時，直接 return [0]\*len(nums)的 List，就可以減少一個 if，增加可讀性。  
btw 這個解法在 leetcode 上，Runtime 18ms, Beats 90.08%, Memory 23.04 MB, Beats 98.35%...好像也沒有真的那麼壞??

#### Second Submission ([code](./07_products_of_array_except_self_02.py)) :

- Language: Python
- Memory: 52.2 MB (leetcode:23.18 MB, Beats 94.02%)
- Runtime: 0.865 seconds (leetcode:24ms, Beats 55.08%)

讀了 NeetCode 的解法後，自己重寫的不用除法的 O(n)解法。思考方式是，在對每個 nums[i]，計算他的之前的元素的乘積(prefix)和在他之後的元素的乘積(suffix)，prefix\*suffix 即為不含自己的所有元素的乘積。為了減少 memory 的用量，不另設 list 分別存 prefix 和 suffix，而是一邊計算 prefix/suffix，直接乘上去。(先由前往後，計算 prefix 並存入 output List，再由後往前，求出 suffix，並直接乘入 output List)

## (08) Valid Sudoku

### Problem

- neetcode: https://neetcode.io/problems/valid-sudoku?list=neetcode150
- leetcode(36): https://leetcode.com/problems/valid-sudoku/description/

### Time / Memory / Notes

#### First Submission ([code](./08_valid_sudoku_01.py)) :

- Language: Python
- Memory: 52 MB (leetcode:17.96 MB, Beats 24.69%)
- Runtime: 1.152 seconds (leetcode:7ms, Beats 36%)

單純就行列、3\*3 的方法做檢查。檢查是否有數字重複的方法是利用 collections 的 Counter

#### Second Submission ([code](./08_valid_sudoku_02.py)) :

- Language: Python
- Memory: 52.3 MB (leetcode:18.08 MB, Beats 5.38%)
- Runtime: 0.843 seconds (leetcode:6ms, Beats 40.9%)

和第一個解法結構相同，單純就行列、3\*3 的方法做檢查，但檢查是否有數字重複的方法是利用 set。掃描每個 group 裡的數字加入 seen，再掃描下一個數字時檢查是否已經 seen 裡。
