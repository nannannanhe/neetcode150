class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        read = set()
        longest = 0
        for num in nums:
            if num-1 in numSet:
                continue
            if num in read:
                continue
            read.add(num)
            streak, current = 1, num
            while current+1 in numSet:
                streak += 1
                current +=1
            longest = max(longest, streak)
        return longest


        