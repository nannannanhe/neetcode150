class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        res = 0
        max_count = 0
        count = defaultdict(int)
        for r in range(len(s)):
            # right point
            count[s[r]] +=1
            max_count = max(max_count, count[s[r]])
            # when replacement count is under k, update res
            if r-l+1 - max_count <= k:
                res = max(res, r-l+1)
            else:
                while r-l+1 - max_count > k:
                    # move left point until the replacement count in under k
                    count[s[l]] -= 1
                    l += 1
                    max_count = max(count.values()) 
        return res