"""
Given a sorted array of distinct integers and a target value, return the index if the target is 
found. If not, return the index where it would be if it were inserted in order.
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        
        while low <= high:
            med = (high + low) // 2
            if nums[med] > target:
                high = med - 1
            elif nums[med] < target:
                low = med + 1
            else:
                return med
        return low