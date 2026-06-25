class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0 # Case 1
        nodup = set(nums) # Case 2: duplicates
        print (nodup)

        longest = 0

        for num in nodup:
            if num-1 not in nodup:
                current = num
                length = 1
                while current + 1 in nodup:
                    current += 1
                    length += 1
                longest = max(length,longest)
        print(longest)
        return longest







        # Brute Force
        # if not nums:
        #     return 0
        # max_length = 1
        # length = 1
        # nums.sort()
        # print(nums)
        # for i in range(1,len(nums)):
        #     if nums[i] == nums[i-1] + 1:
        #         length += 1
        #     elif nums[i] != nums[i-1]:
        #         length = 1
        #     max_length = max(max_length,length)
        # print(max_length)
        # return max_length

        