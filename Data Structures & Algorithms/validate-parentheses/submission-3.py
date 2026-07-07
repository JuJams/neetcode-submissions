class Solution:
    def isValid(self, s: str) -> bool:
        # time: O(n)
        # space: O(n)
        stack = []
        # hashmap of symbols
        valid = {'(':')','{':'}','[':']'}
        for sym in s:
            if sym in valid:
                stack.append(sym)
            else:
                if not stack or valid[stack[-1]] != sym:
                    return False
                stack.pop()
                
        return len(stack) ==0
        
        