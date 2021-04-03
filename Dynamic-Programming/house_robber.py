"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount
of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses 
have security systems connected and it will automatically contact the police if two adjacent houses 
were broken into on the same night.Given an integer array nums representing the amount of money of 
each house, return the maximum amount of money you can rob tonight without alerting the police.
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        max_money = [0] * (len(nums)+1)
        for index, value in enumerate(nums):
            if index == 0:
                max_money[1] = value
            else:
                max_money[index+1] = max(max_money[index], max_money[index-1] + value)
                
        return max_money[len(nums)]