class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # time: O(n)
        # space: O(n)
        result = [0] * len(temperatures)
        stack = [] # addign a pair of temp and index
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackt, stacki = stack.pop()
                result[stacki] = (i - stacki)
            stack.append([temp,i])
        return result