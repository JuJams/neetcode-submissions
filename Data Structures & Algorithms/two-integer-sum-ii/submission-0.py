class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        while left < right:
            val1 = numbers[left] #1
            val2 = numbers[right] #4
            if val1 + val2 == target:
                return [left+1,right+1]
            elif val1 + val2 < target:
                left += 1
            else:
                right -=1
                

        