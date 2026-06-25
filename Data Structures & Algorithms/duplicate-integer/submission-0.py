class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Optmised solution using hash maps
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        seen = {}
        for i in range(0,len(nums)):
            if nums[i] in seen:
                return True
            else:
                seen[nums[i]] = True
        return False
        
            
        # Brute Force 
        # Time Complexity: O(n^2)
        # Space Complexity: O(n)

        # for i in range(0,len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False