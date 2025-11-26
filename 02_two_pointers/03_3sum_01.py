class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        output = []
        for i in range(len(nums)-2):
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue
            target = 0 - sorted_nums[i]
            j, k = i+1, len(nums) -1
            while j < k:
                if sorted_nums[j] + sorted_nums[k] > target:
                    k -= 1
                elif sorted_nums[j] + sorted_nums[k] < target:
                    j += 1
                elif sorted_nums[j] + sorted_nums[k] == target:
                    output.append([sorted_nums[i], sorted_nums[j], sorted_nums[k]])
                    k -=1
                    j +=1
        
        return [list(t) for t in {tuple(item) for item in output}]
        