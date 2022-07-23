from collections import deque

class Solution:
    
    def countSmaller(self, nums: List[int]) -> List[int]:
        nums = list(enumerate(nums))
        counts = [0] * len(nums)
        
        def daq(le, ri):
            if le >= ri:
                return nums[le:ri+1]
            
            mid = (le + ri) >> 1
            
            right = daq(mid+1, ri) 
            left = daq(le, mid)
            
            ret = deque()
            while True:
                if not left:
                    return right + list(ret)
                if not right:
                    return left + list(ret)
                if left[-1][1] > right[-1][1]:
                    counts[left[-1][0]] += len(right)
                    ret.appendleft(left.pop())
                else:
                    ret.appendleft(right.pop())
            
            return list(ret)
        
        
        daq(0, len(nums) - 1)
        
        return counts