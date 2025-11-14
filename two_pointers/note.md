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
