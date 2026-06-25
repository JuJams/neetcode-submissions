class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        print (result)

        # Making a preifx array
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
        print(result)

        # Making suffix array for everythingt hat is to the right of i
        suffix = 1
        for i in range(n-1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        return result       




        # # Brute Force
        # # Time Complexity: O(n^2)
        # # Space Complexity: O(n)
        # result = []
        # for i in range(len(nums)):
        #     product = 1
        #     for j in range(len(nums)):
        #         if i != j:
        #             product *= nums[j]
        #     result.append(product)
        # return result