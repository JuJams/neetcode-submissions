class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Optimal Solution
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False
        
        count1 = [0] * 26
        count2 = [0] * 26

        for i in range(n1):
            count1[ord(s1[i])-ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1

        if count1 == count2:
            return True

        for i in range(n1,n2):
            count2[ord(s2[i])-ord('a')] += 1
            count2[ord(s2[i-n1])-ord('a')] -= 1

            if count1 == count2:
                return True
        return False





        #  Brute Force
        # n = len(s1)
        # m = len(s2)

        # for i in range(m-n+1):
        #     sub = s2[i:i+n]
        #     if sorted(sub) == sorted(s1):
        #         return True
        # return False

       
        