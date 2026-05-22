class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        group = defaultdict(int)

        for num in nums:
            group[num] +=1

        groupSorted = dict(sorted(group.items(), key=lambda item: item[1]))

        return list(groupSorted.keys())[-k:]
