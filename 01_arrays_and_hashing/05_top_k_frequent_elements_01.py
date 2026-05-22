from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = defaultdict(int)
        for num in nums:
            count_map[num] += 1
        sorted_items = sorted(count_map.items(), key=lambda item:item[1], reverse=True)
        result = []
        for i in range(k):
            result.append(sorted_items[i][0])
        return result
        
