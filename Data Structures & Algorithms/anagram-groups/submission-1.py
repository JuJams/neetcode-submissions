class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        same = {}
        for i in range(0,len(strs)):
            sort_i = sorted(strs[i])
            key = ''.join(sort_i)
            # print(key)
            if key not in same:
                same[key] = []
                print(same)
            same[key].append(strs[i])
            print(same)
        return(list(same.values()))