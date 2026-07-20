class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = nums1
        b = nums2
        total = len(a) + len(b)
        half = total//2

        if len(b) < len(a):
            a,b = b,a

        left = 0
        right = len(a) - 1

        while True:
            i = (left + right) // 2 # a
            j = half - i - 2 #b
            aleft = a[i] if i >= 0 else float("-infinity")
            aright = a[i+1] if (i+1) < len(a) else float ("infinity")
            bleft = b[j] if j >= 0 else float("-infinity")
            bright = b[j+1] if (j+1) < len(b) else float("inifinity")

            # checkign if partion is correct
            if aleft <= bright and bleft <= aright:
                # odd length
                if total % 2:
                    return min(aright, bright)
                # even length
                return ((max(aleft, bleft) + min(aright, bright))/2)
            elif aleft > bright:
                right = i - 1
            else:
                left = i + 1
