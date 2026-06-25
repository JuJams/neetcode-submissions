class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Optimal Solution: Use a hashmap
        seen = {}
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen[nums[i]] = i # {5:0}
        for j in range(len(nums)):
            diff = target - nums[j] 
            if (diff in seen and j != seen[diff]):
                return [min(seen[diff],j), max(seen[diff],j)]

    
        
        
            


        # # Brute Force
        # # Time complexity: O(n^2)
        # # Space Complexity: O(1)
        # for i in range(0,len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]