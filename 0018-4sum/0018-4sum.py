class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def kSum(nums, target, k):
            res = []
            
            if not nums:
                return res
            
            # Optimization: If the target is impossible to reach given the 
            # current smallest and largest elements, terminate early.
            average_value = target // k
            if average_value < nums[0] or nums[-1] < average_value:
                return res
            
            # Base case: When k reduces to 2, use the standard 2Sum approach
            if k == 2:
                return twoSum(nums, target)
            
            for i in range(len(nums)):
                if i == 0 or nums[i - 1] != nums[i]:
                    for subset in kSum(nums[i + 1:], target - nums[i], k - 1):
                        res.append([nums[i]] + subset)
            
            return res

        def twoSum(nums, target):
            res = []
            left, right = 0, len(nums) - 1
            
            while left < right:
                curr_sum = nums[left] + nums[right]
                
                if curr_sum == target:
                    res.append([nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif curr_sum < target:
                    left += 1
                else:
                    right -= 1
                    
            return res

        nums.sort()
        return kSum(nums, target, 4)