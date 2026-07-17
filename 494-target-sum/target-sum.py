class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(index, total):
            # Base case
            if index == len(nums):
                return 1 if total == target else 0

            # Check if already computed
            if (index, total) in memo:
                return memo[(index, total)]

            # Choose '+' or '-'
            add = dfs(index + 1, total + nums[index])
            subtract = dfs(index + 1, total - nums[index])

            memo[(index, total)] = add + subtract
            return memo[(index, total)]

        return dfs(0, 0)
        