class Solution:
    def twoSum(self, nums, target):
        n = len(nums)
        # Check every number
        for i in range(n):
            # Check every number that comes AFTER it
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]