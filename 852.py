class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        i = 0
        while i < len(A):
            if A[i] < A[i+1]:
                i += 1
            else:
                result = i
                break
                
        return result