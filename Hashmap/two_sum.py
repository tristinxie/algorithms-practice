"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement_index = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in complement_index:
                return [complement_index[complement], index]
            else:
                complement_index[num] = index