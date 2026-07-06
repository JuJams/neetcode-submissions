class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        while left < right:
            while left < right and not self.alphanum(s[left]):
                left += 1
            while right > left and not self.alphanum(s[right]):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
        

    def alphanum(self,s):
        return (ord('A') <= ord(s) <= ord('Z') or 
        (ord('a') <= ord(s) <= ord('z')) or
        (ord('0') <= ord(s) <= ord('9')))

