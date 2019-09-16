class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        result = 0
        while i < len (nums):
            if i%2 == 0:
                result = result + nums[i]
            i += 1
        
        return result