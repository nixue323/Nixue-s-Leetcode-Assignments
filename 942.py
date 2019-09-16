class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        min = 0
        max = len(S)
        i = 0
        result = []
        while i < len(S):
            if S[i] == 'I':
                result.append(min)
                min += 1
            if S[i] == 'D':
                result.append(max)
                max -= 1
            i += 1
        result.append(min)
        
        return result
        
        