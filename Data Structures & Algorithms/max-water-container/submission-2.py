class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            height = min(heights[right],heights[left])
            width = right - left
            water = width * height
            area = max(area, water)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1 
        return area
            
