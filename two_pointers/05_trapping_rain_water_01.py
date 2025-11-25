class Solution:
    def trap(self, height: List[int]) -> int:
        prefix_max = [0]
        max_height = 0
        for i in range(1, len(height)):
            max_height = max(max_height, height[i-1])
            prefix_max.append(max_height)
            

        suffix_max = [0]
        max_height = 0
        for i in range(len(height)-2, -1, -1):
            max_height = max(max_height, height[i+1])
            suffix_max.append(max_height)
        suffix_max.reverse()

        water = 0
        for i in range(len(height)):
            water += max(0, min(prefix_max[i], suffix_max[i])-height[i])
        return water
        