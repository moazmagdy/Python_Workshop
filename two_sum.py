#Leetcode problem No. 1:
""""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""
import operator
import functools

nums = [3,2,4]
target = 6
def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        x = [[i,j] for i in range(len(nums)) for j in range(1, len(nums)) if ((nums[i]+nums[j])==target)and (i!= j)]
        return functools.reduce(operator.iconcat,[x],[])


print(twoSum(nums, target))