class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Optimal solution is to use a hashmap
        # Time complexity is O(m+n)
        # Space complexity is O(k) where k is the unique number of characters
        if len(s) != len(t):
            return False
        ana = {}  
        for letter in s:
            if letter in ana:
                ana[letter] += 1
            else:
                ana[letter] = 1
        for letter in t:
            if letter in ana:
                ana[letter] -= 1
            else:
                return False
        for i in ana:
            if ana[i] != 0:
                return False
        return True


















        # same = {}
        # if len(s) != len(t):
        #     return False
        # for i in range(len(s)):
        #     char = s[i]
        #     if char not in same:
        #         same[char] = 1
        #     else:
        #         same[char] += 1
        # for i in range(len(t)):
        #     check = t[i]
        #     if check not in same:
        #         return False
        #     same[check] -= 1
        # for i in same:
        #     if same[i] != 0:
        #         return False
        # return True


        # # # Brute Force
        # # # Time complexity: O(log n)
        # # # Space Complexity: O(n)
        # # s_string = ''.join(sorted(s))
        # # t_string = ''.join(sorted(t))
        # # if s_string == t_string:
        # #     return True
        # # return False
