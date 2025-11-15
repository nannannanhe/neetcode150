class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for index1 in range(len(numbers)-1):
            if index1 > 0 and numbers[index1-1] == numbers[index1]:
                continue
            for index2 in range(index1+1, len(numbers)):
                if numbers[index1] + numbers[index2] == target:
                    return [index1+1, index2+1]
                if numbers[index1] + numbers[index2] > target:
                    break
        