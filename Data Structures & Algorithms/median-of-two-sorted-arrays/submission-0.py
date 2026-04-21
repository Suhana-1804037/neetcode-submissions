class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A)+len(B)
        half = total//2

        if len(A)>len(B):
            A,B = B,A
        l, r = 0, len(A)-1
        while True:
            AiMid = (l+r)//2
            Bi = half - AiMid -2

            Aleft = A[AiMid] if AiMid>=0 else float("-infinity")
            Aright = A[AiMid+1] if AiMid+1<len(A) else float("infinity")
            Bleft = B[Bi] if Bi>=0 else float("-infinity")
            Bright = B[Bi+1] if Bi+1<len(B) else float("infinity")

            if Aright>=Bleft and Bright>=Aleft:
                if total%2:
                    return min(Aright, Bright)
                else:
                    return ((max(Aleft, Bleft)+min(Bright, Aright))/2)
            elif Aleft>Bright:
                r = AiMid-1
            else:
                l = AiMid +1
