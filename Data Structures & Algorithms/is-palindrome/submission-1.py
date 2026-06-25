class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = []
        for character in s:
            if ord(character) > 64 and ord(character) < 90:
                small = ord(character) + 32
                letter = chr(small)
                result.append(letter)
            elif ord(character) > 96 and ord(character) < 123:
                result.append(character)
            elif ord(character) > 47 and ord(character) < 58:
                result.append(character)
            else:
                continue
        print(result)

        left = 0
        right = len(result) - 1

        while left < right:
            if result[left] != result[right]:
                return False
            left += 1
            right -= 1
        return True
