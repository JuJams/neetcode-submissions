class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        chars = {'(':')','{':'}','[':']'}

        for each in s:
            if each in chars:
                stack.append(each)
            else:
                if not stack or chars[stack[-1]] != each:
                    return False
                stack.pop()
                #print(stack)
        
        return len(stack) == 0
