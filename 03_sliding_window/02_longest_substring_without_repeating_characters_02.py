class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        l, r = 0, 0
        word_set = set()
        longest = 0
        while r < len(s):
            while s[r] in word_set:
                # slide
                word_set.remove(s[l])
                l += 1
            word_set.add(s[r])
            longest = max(longest, len(word_set))
            r += 1
        return longest