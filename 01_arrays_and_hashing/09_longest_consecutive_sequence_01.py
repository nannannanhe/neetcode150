import heapq
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        heapq.heapify(nums)
        former = heapq.heappop(nums)
        cons_count = 1
        max_count = 1
        while nums:
            now = heapq.heappop(nums)
            if now == former:
                continue
            if now == former +1:
                cons_count += 1
            else:
                cons_count = 1
            former = now
            max_count = max(max_count, cons_count)
        return max_count

        