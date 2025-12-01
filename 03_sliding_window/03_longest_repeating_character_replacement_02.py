from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, k
        res = k
        c = Counter(s[l:r+1])
        top_char, top_count = c.most_common(1)[0]
        while l<len(s) and r < len(s):
            if (r-l+1) - top_count <= k:
                res = max(res, r-l+1)
                r += 1
                if r < len(s):
                    c[s[r]] +=1
                    if top_count < c[s[r]] :
                        top_char = s[r]
                        top_count = c[s[r]]
            else:
                c[s[l]] -= 1
                top_char, top_count = c.most_common(1)[0]
                l += 1
        return res