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

分別定義 index1 和 index2，往後一個一個找。O(n^2)  
由於輸入是 non-decreasing sorted，當相加大於 target 時就 break，節省時間。  
原先沒有加 line4-5 的判斷時，在 leetcode 21th testcase 會 TLE，原因為在找到正解(在相當長的 List 的最後)前，前面會經過大量的相同元素。在以 index1 為首往後掃過所有資料仍找不到滿足的 index2 時，即代表 numbers[index1]沒有對應的值，因此若 index+1 的值仍相同時，可以跳過。追加此判斷後通過。

#### 2nd Submission ([code](./02_two_integer_sum_ii_02.py)) :

- Language: Python
- Memory: 51.9 MB (leetcode:18.72 MB, Beats 9.18%)
- Runtime: 0.846 seconds (leetcode:7ms, Beats 23.67%)

讀過 NeetCode 的解說後重寫。由於數列是 non-decreasing 的，  
利用 two-pointers，一個在最前，一個在最後，  
當相加的值大於 target，即表示目前的值太多，令值最大的右側往左移一格，  
而當相加的值小於 target，表示目前的值太小，令值最小的左側往右移一格，以求得正確的 pair。O(n)

## (03) 3Sum

### Problem

- neetcode: https://neetcode.io/problems/three-integer-sum/question
- leetcode(15): https://leetcode.com/problems/3sum/description/

### Time / Memory / Notes

#### First Submission ([code](./03_3sum_01.py)) :

- Language: Python
- Memory: 52.3 MB (leetcode:23.45 MB, Beats 5.05%)
- Runtime: 0.795 seconds (leetcode:483ms, Beats 79.33%)

我的解法是上一題 Two Integer Sum II 的延伸題的感覺。  
由於 output 不需要原來的 index，直接先對原來的 nums 排序，在 non-decreasing 的狀況下，分三個點:i, j, k。

- i: 從最前到最後，如果後面掃到的值前面已經掃過就跳過
- j，k: 想法同上一題的 two pointer，合計值(target)為 0-sorted_nums[i]的值(因三個數相加為零)。但這次由於會有複數解，在找到合適的解後，j 往後一位，k 往前一位，繼續找可能的解。

#### 2nd Submission ([code](./03_3sum_02.py)) :

- Language: Python
- Memory: 51.9 MB (leetcode:20.73 MB, Beats 37.27%)
- Runtime: 0.932 seconds (leetcode:375ms, Beats 97.37%)

在參考 NeetCode 的解答後，發現有可以改善的地方

- 可以直接對 List 做 sort()，不用另開 List 來存
- 當 nums[i]的值大於零時，在 non-decreasing 的情況不可能找到合為零的解，可直接 break
- 原來的解法當 i 之後的 List 裡有重複值時，會同樣找出放進 output 裡，因此需要先轉為 tuple 放進 set 再轉回 List 來排除重複的解。可直接在原來的判斷裡加上 while，使 j 位移到不重複的值來解決原先會有重複解的問題

改善上述三點後，NeetCode 和 LeetCode 上在 Memory 用量上都有改善。時間上則是只有 LeetCode 大幅改善，推測可能是有對應到部分測資?

## (04) Container With Most Water

### Problem

- neetcode: https://neetcode.io/problems/max-water-container/question
- leetcode(11): https://leetcode.com/problems/container-with-most-water/description/

### Time / Memory / Notes

#### First Submission ([code](./04_container_with_most_water_01.py)) :

- Language: Python
- Memory: 52.1 MB (leetcode:TLE on 55th testcase)
- Runtime: 0.828 seconds (leetcode:TLE on 55th testcase)

一時想不到聰明的解法，直覺用 BruteForce 解。第一個點 i 從 heights[0~n-1]，第二個點 j 從 heights[i+1~n]，去算 min(heights[i], heights[j]) \* (j-i)的乘積(即 container 的容量)，找最大值。在其中之一的值為 0 時跳過以減少一點計算量。NeetCode 過了但 LeetCode TLE。O(n^2)

#### 2nd Submission ([code](./04_container_with_most_water_02.py)) :

- Language: Python
- Memory: 52 MB (leetcode: 28.62 MB, beats 23.91%)
- Runtime: 0.894 seconds (leetcode: 111 ms, beats 21.07%)

看了 NeetCode 的解說，用 2 pointers 重寫。  
想法是，在兩頭定義 l 和 r 兩個 pointer，此時的寬是最大的，如果剛好兩頭的 height 是高的時，就能得到最大的容積。而在找下一個可能的更大的容積時，寬由於 pointer 的移動，一定會變小一格；在高度方面，將 l 和 r 中較短的那個 pointer 往另一端移動，若下一格的高較目前高，則可能獲得比前一格取得的更大的容積。一直掃到兩點交錯。O(n)  
因為這題歸類在 two pointers，其實一開始是有想能不能用 two pointer 來做的，但沒想到上面的解法...就算想在兩頭定義 l 和 r，也想不到這樣的移動可以得到最大解。可能就是需要經驗吧

## (05) Trapping Rain Water

### Problem

- neetcode: https://neetcode.io/problems/trapping-rain-water/question
- leetcode(42): https://leetcode.com/problems/trapping-rain-water/description/

### Time / Memory / Notes

#### First Submission ([code](./05_trapping_rain_water_01.py)) :

- Language: Python
- Memory: 52.3 MB (leetcode: 19.39 MB, beats 38.63%)
- Runtime: 0.84 seconds (leetcode: 31 ms, beats 19.83%)

看了 NeetCode 在 description 裡給的 Hint 才解出來。  
想法是對每個點求他的積水量，而為了求積水量，先對每個點找出他向左(prefix)、向右(suffix)分別的最大值，該點的積水量為 min(prefix[i], suffix[i])-height[i]，當值小於零則表示不會積水。  
...怎麼可能在 30 分鐘裡想到??至少我是想不到 orz

#### 2nd Submission ([code](./05_trapping_rain_water_02.py)) :

- Language: Python
- Memory: 52.2 MB (leetcode: 19.27 MB, beats 69.23%)
- Runtime: 0.82 seconds (leetcode: 17 ms, beats 43.61%)

聽了 NeetCode 的解說，用 two pointers 重寫。  
想法是，由於在求單點的積水時，只需要知道 min(prefix, suffix)，所以，只需要在兩端點定義 l, r，並以其值為 max_l, max_r，從較小的那端向另一端計算過去即可。各點的積水量仍然是當下的 min(max_l, max_r)-height[當下的點]。
