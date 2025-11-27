class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        word_map = {}
        longest = 0
        
        for r in range(len(s)):
            if s[r] in word_map:
                l = max(word_map[s[r]] + 1, l)
            word_map[s[r]] = r
            longest = max(longest, r - l +1)
        return longest