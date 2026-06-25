class Solution:
    # This is the optimal solution
    # Time Complexity: O(m)
    # Space Compelxity: O(m)
    def encode(self, strs: List[str]) -> str:
        encode = ''
        for i in range(len(strs)):
            length = len(strs[i])
            encode += str(length) + '#' + strs[i]
        print(encode)
        return encode

    def decode(self, s: str) -> List[str]:
        # Time Complexity: O(m)
        # Space Compelxity: O(m+n)
        decode = []
        i = 0
        while i < len(s):
            length_str = ''
            while s[i] != '#':
                length_str += s[i]
                i += 1
            length = int(length_str)
            print(length)
            i += 1
            word = ''
            for _ in range(length):
                word += s[i]
                i += 1
            decode.append(word)
        return decode

