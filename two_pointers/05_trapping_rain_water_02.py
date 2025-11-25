class Solution:
    def trap(self, height: List[int]) -> int:
        water=0
        l, r = 0, len(height)-1
        max_l, max_r = height[l], height[r]
        while l < r:
            if max_l <= max_r:
                l += 1
                water += max(0, max_l-height[l])
                max_l = max(max_l, height[l])
            else:
                r -= 1
                water += max(0, max_r-height[r])
                max_r = max(max_r, height[r])
        return water
        