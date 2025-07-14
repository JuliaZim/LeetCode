class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if nums[i]+nums[j] == target:
                    ind = [i, j]
                    return ind
solution = Solution()
solution.twoSum([2, 7, 11, 15], 9)
        