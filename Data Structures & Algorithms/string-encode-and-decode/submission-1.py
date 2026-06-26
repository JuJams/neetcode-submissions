class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""
        if len(strs) == 0:
            return ""
        count = 0
        for word in strs:
            count = len(word)
            encode += str(count) + '#' + word
            #print(count)
        print(encode)
        return encode
    
    def decode(self, s: str) -> List[str]:
        decode = []
        i = 0
        while i < len(s): # 0
            j = i # 0 #1
            while s[j] != "#":
                j += 1 
            length = int(s[i:j]) 
            word = s[j+1:j+1+length]
            decode.append(word)
            i = j+1+length
        return decode
