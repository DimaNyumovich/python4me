class Solution(object):
    def searchInsert(self, nums: list[int], target: int):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for item in nums:
            if item >= target:
                return nums.index(item)
        return len(nums)




sol = Solution()
print(sol.searchInsert([1,3,5,6], 7))