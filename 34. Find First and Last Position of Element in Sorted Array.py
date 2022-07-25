class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)-1
        
        while left <= right:
            mid = left + (right-left)//2
            
            if nums[mid] == target:
                l = r = mid
                while l >= 0 and nums[mid] == nums[l]:
                    l -= 1
                while r <= right and nums[mid] == nums[r]:
                    r += 1
                
                return [l+1, r-1]
            
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return [-1, -1]
                