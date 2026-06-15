class Solution:
    def twoSum(self, nums, target):
        seen = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in seen:
                return [seen[complement] + 1, i + 1]

            seen[nums[i]] = i