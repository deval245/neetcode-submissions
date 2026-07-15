class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()  # Step 1: Sort array
        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicate first elements
                continue

            left, right = i + 1, len(nums) - 1  # Two pointers

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])  # Found triplet

                    # Skip duplicate second and third elements
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif total < 0:
                    left += 1  # Need bigger sum
                else:
                    right -= 1  # Need smaller sum

        return result
