from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = defaultdict(int)
        for num in nums:
            count_map[num] += 1
        sorted_items = sorted(count_map.items(), key=lambda item:item[1], reverse=True)
        return [item[0] for item in sorted_items[0:k]]
        
