class Solution:
    def search(self, nums: List[int], target: int) -> int:
        check = -1
        for i in range(len(nums)):
            if nums[i] == target:
                check = i
                return check
        return check