class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        same = {}
        for i in range(len(strs)):
            count = [0] * 26
            for j in range(len(strs[i])):
                char = strs[i][j]
                index = ord(char) - ord('a')
                count[index] += 1
            key = tuple(count)
            if key not in same:
                same[key] = []
            same[key].append(strs[i])

        return(list(same.values()))














        # # Most optimal solution using hashmap and no sort
        # # Time Complexity: O(mn)
        # # Space Complexity: O(m)
        # same = {}
        # for i in range(len(strs)):
        #     # making an array for 26 character
        #     count = [0] * 26
        #     for j in range(len(strs[i])):
        #         char = strs[i][j]
        #         index = ord(char) - ord('a')
        #         count[index] += 1
        #     key = tuple(count)
        #     print (key)
        #     if key not in same:
        #         same[key] = []
        #     same[key].append(strs[i])
        # print(same)
        # return(list(same.values()))
        

        # # Sorting is not the most optimal
        # # Time complexity: O(n m log m)
        # # Space Complexity: O(mn)
        # same = {}
        # for i in range(0,len(strs)):
        #     sort_i = sorted(strs[i])
        #     key = ''.join(sort_i)
        #     # print(key)
        #     if key not in same:
        #         same[key] = []
        #     same[key].append(strs[i])
        # return(list(same.values()))