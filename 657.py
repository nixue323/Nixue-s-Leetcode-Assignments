class Solution:
    def judgeCircle(self, moves: str) -> bool:
        d = {'L':0,'R':0,'U':0,'D':0}
        for i in moves:
            d[i] += 1
        
        return d['L'] == d['R'] and d['U'] == d['D']
