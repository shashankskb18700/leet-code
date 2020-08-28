class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        import math
        lo=0
        hi=len(nums)-1
        while lo<=hi:
            mid=math.trunc((hi+lo)/2)
            mid_val=nums[mid]
            if target ==mid_val:
                return mid
            elif target>mid_val:
                lo=mid+1
            else:
                hi=mid-1
        return lo
