class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        l, r = 0, 1
        word_set = {s[0]}
        longest = 1
        while r < len(s):
            if s[r] in word_set:
                # reset
                l = l+1
                r = l
                word_set = {s[l]}
            else:
                word_set.add(s[r])
                longest = max(longest, len(word_set))
            r += 1
        return longest
