## (01) Valid Palindrome

### Problem

- neetcode: https://neetcode.io/problems/is-palindrome?list=neetcode150
- leetcode(125): https://leetcode.com/problems/valid-palindrome/description/

### Time / Memory / Notes

#### First Submission ([code](./01_valid_palindrome_01.py)) :

- Language: Python
- Memory: 51.9 MB (leetcode:23.75 MB, Beats 5.41%)
- Runtime: 0.849 seconds (leetcode:5ms, Beats 88.33%)

先對 s 做前處理，取出 alphanumerics 的元素並全轉為小寫後，  
利用 List[::-1]得到順序反轉的 List，然後比較反轉前後 join 得到的字串。  
速度不差，但沒有練習到這章的 title, two pointers。囧

#### 2nd Submission ([code](./01_valid_palindrome_02.py)) :

- Language: Python
- Memory: 52.1 MB (leetcode:23.17 MB, Beats 17.46%)
- Runtime: 0.797 seconds (leetcode:9ms, Beats 44.99%)

two pointers 的解法

## (02) Two Integer Sum II

### Problem

- neetcode: https://neetcode.io/problems/two-integer-sum-ii?list=neetcode150
- leetcode(167): https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

### Time / Memory / Notes

#### First Submission ([code](./02_two_integer_sum_ii_01.py)) :

- Language: Python
- Memory: 52.2 MB (leetcode:18.54 MB, Beats 58.88%)
- Runtime: 0.883 seconds (leetcode:11ms, Beats 6.19%)

分別定義 index1 和 index2，一個一個找。  
由於輸入是 non-decreasing sorted，當相加大於 target 時就 break，節省時間。  
原先沒有加 line4-5 的判斷時，在 leetcode 21th testcase 會 TLE，原因為在找到正解(在相當長的 List 的最後)前，前面會經過大量的相同元素。在以 index1 為首往後掃過所有資料仍找不到滿足的 index2 時，即代表 numbers[index1]沒有對應的值，因此若 index+1 的值仍相同時，可以跳過。追加此判斷後通過。
