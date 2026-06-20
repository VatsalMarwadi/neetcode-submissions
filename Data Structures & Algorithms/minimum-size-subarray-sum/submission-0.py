class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        sum = 0
        res = float('inf')
        for i in range(len(nums)):
            sum += nums[i]
            while sum >= target:
                res = min(res, i - l + 1)
                sum -= nums[l] 
                l += 1
        return 0 if res == float('inf') else res