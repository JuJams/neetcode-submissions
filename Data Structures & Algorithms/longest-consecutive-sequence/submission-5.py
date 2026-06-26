class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        check = set(nums)
        print(check)
        for num in nums:
            if num-1 not in check:
                current = num
                streak = 1
                while current+1 in check:
                    current += 1
                    streak += 1
                longest = max(longest,streak)
        return longest


