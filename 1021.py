class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        i = 0
        primitive = ""
        result = ""
        left = 0
        right = 0
        while i < len(S):
            primitive += S[i]
            if S[i] == "(":
                left += 1
            if S[i] == ")":
                right += 1
            if left == right:
                result += primitive[1:-1]
                left = 0
                right = 0
                primitive = ""
            i += 1
        
        return result