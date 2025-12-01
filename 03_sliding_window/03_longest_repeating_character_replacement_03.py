from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, k
        res = min(k+1, len(s))
        c = Counter(s[l:r+1])
        top_count = max(c.values())
        while l < len(s) and r < len(s):
            if r-l+1 - top_count <= k:
                # upgrade res
                res = max(res, r-l+1)
                # move right point
                r += 1
                # if still in range, upgrade top_count
                if r < len(s):
                    c[s[r]] +=1
                    top_count = max(top_count, c[s[r]])
            else:
                # move left point and upgrade top_count
                c[s[l]] -=1
                top_count = max(c.values())
                l += 1
        return res