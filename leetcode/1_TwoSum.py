class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, num in enumerate(nums):
            if target - num in nums[i+1:]:
                second_num = target - num
                second_ind = nums[i + 1:].index(second_num) + 1 + i
                return [i, second_ind]



sols = Solution()
# print(sols.twoSum([2, 7, 11, 15], 9))
# print(sols.twoSum([3,2,4], 6))
print(sols.twoSum([3,3], 6))