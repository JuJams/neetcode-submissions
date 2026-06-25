class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Optimal Solution: Use a hashmap
        seen = {}
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen[nums[i]] = i
        for j in range(len(nums)):
            difference = target - nums[j]
            if difference in seen:
                if j != seen[difference]:
                    return [min(j, seen[difference]), max(j, seen[difference])]
            


        # # Brute Force
        # # Time complexity: O(n^2)
        # # Space Complexity: O(1)
        # for i in range(0,len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]