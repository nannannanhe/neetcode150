class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_amount = 0
        for i in range(len(heights)-1):
            if heights[i] == 0:
                continue
            for j in range(i+1, len(heights)):
                if heights[j] == 0:
                    continue
                max_amount = max(max_amount, min(heights[i], heights[j])*(j-i))
        return max_amount
        