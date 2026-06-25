class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Two - pointer approach
        water = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            height = min(heights[left],heights[right])
            width = right - left
            area = height * width
            water = max(water, area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        #  print(water)
        return water
        





        # # Brute Force Solution: O(n^2)
        # #result = []
        # water = 0
        # for i in range(len(heights)):
        #     for j in range (i+1, len(heights)):
        #         area = min (heights[i], heights[j]) * (j-i)
        #         #result.append(area)
        #         water = max(water, area)
        # #print(result)
        # #print (water)
        # return water
        