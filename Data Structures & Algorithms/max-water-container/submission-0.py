class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #result = []
        water = 0
        for i in range(len(heights)):
            for j in range (i+1, len(heights)):
                area = min (heights[i], heights[j]) * (j-i)
                #result.append(area)
                water = max(water, area)
        #print(result)
        #print (water)
        return water
        