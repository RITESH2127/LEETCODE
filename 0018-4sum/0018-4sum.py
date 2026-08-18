class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n - 3):
            # Skip duplicates for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                # Skip duplicates for the second number
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # Use two pointers for the remaining two numbers
                left, right = j + 1, n - 1
                
                while left < right:
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]

                    if current_sum == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])

                        # Skip duplicates for the third number (left pointer)
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        # Skip duplicates for the fourth number (right pointer)
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        # Move both pointers inward after finding a valid quadruplet
                        left += 1
                        right -= 1
                        
                    elif current_sum < target:
                        # Sum is too small, we need a larger number
                        left += 1
                    else:
                        # Sum is too big, we need a smaller number
                        right -= 1

        return res