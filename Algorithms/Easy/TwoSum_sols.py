"""
You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Constraints:

- 2 <= nums.length <= 104
- 109 <= nums[i] <= 109
-109 <= target <= 109

Only one valid answer exists.

"""
#1st. solution:
class Solution(object):
    def twoSum(self, nums, target):
        results = []
        indexes = []
        for index in range(len(nums)):
            for subindex in range(len(nums)):
                if index != subindex:
                    current_element = nums[index]
                    next_element = nums[subindex]
                    result = current_element + next_element
                    if result == target:
                        indexes.append(index)
                        indexes.append(subindex)
                        return indexes

# Optimised solution:
class Solution(object):
    def twoSum(self, nums, target):
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i

