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
