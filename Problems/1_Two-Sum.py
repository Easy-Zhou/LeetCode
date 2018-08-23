#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/23 22:02
# @Author  : Zhou
# @File    : 1_Two-Sum.py
# @IDE     : PyCharm
# @Description: 1_Two-Sum
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            first_num = nums[i]
            second_num = target - first_num
            if second_num in nums[i+1:]:
                return [i, nums[i+1:].index(second_num) + i+1]


test = Solution()
print(test.twoSum([3, 3], 6))