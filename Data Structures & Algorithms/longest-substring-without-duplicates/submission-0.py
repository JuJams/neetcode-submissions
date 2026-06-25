class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        setty =  set() # "zxyzxyz"
        print(setty) # {}
        left = 0 # 1
        result = 0 # 1 2 3
        for right in range(len(s)):
            print(setty) # {z,x,y}
            while s[right] in setty: 
                setty.remove(s[left])
                left += 1
            setty.add(s[right]) # {x,y}
            result = max(result, right - left + 1) # 1 3
        print(setty) # {x,y}
        return result





