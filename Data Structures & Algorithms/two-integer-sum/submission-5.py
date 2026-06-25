class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # optimal
        # time: O(n)
        # space: O(n)
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num # 6 5 4
            if diff in seen: # _ _ yes
                return [seen[diff], i] # [0, 2]
            seen[num] = i # {4: 0, 5: 1}


        # found = {}
        # for i in range(len(nums)):
        #     if nums[i] not in found:
        #         found[nums[i]] = i # {3: 0, 4: 1, 5: 2, 6: 3}
        # for j in range(len(nums)):
        #     diff = target - nums[j]
        #     if diff in found and found[diff] != j:
        #         return [j,found[diff]]
        

        # # brute force
        # # time: O(n^2)
        # # space: O(1)
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
        # # Optimal Solution: Use a hashmap
        # seen = {}
        # for i in range(len(nums)):
        #     if nums[i] not in seen:
        #         seen[nums[i]] = i # {5:0}
        # for j in range(len(nums)):
        #     diff = target - nums[j] 
        #     if (diff in seen and j != seen[diff]):
        #         return [min(seen[diff],j), max(seen[diff],j)]

    
        
        
            


        # # # Brute Force
        # # # Time complexity: O(n^2)
        # # # Space Complexity: O(1)
        # # for i in range(0,len(nums)):
        # #     for j in range(i+1, len(nums)):
        # #         if nums[i] + nums[j] == target:
        # #             return [i,j]