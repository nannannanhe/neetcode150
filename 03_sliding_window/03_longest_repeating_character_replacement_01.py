from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, k
        res = k
        while l<len(s) and r < len(s):
            substr = s[l:r+1]
            top_char, top_count = Counter(substr).most_common(1)[0]
            if len(substr) - top_count <= k:
                res = max(res, len(substr))
                r += 1
            else:
                l += 1
        return res
