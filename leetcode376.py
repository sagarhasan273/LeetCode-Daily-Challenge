class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        def calculate(nums, index, isUp):
            maxCount = 0
            for i in range(index+1, len(nums)):
                if (isUp and nums[i] > nums[index]) or (not isUp and nums[i] < nums[index]):
                    maxCount = max(maxCount, 1+calculate(nums, i, not isUp))
            
            return maxCount
        
        if len(nums) < 2:
            return len(nums)
        return 1 + max(calculate(nums, 0, False), calculate(nums, 0, True))