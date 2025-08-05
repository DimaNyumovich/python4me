class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
            print(nums)
        return index, nums



    def removeElement1(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        nums.sort()
        ind_start = None
        ind_end = None
        length_list = len(nums)
        for i in range(length_list):
            if nums[i] == val and not ind_start:
                ind_start = i
                ind_end = i
            elif nums[i] == val and ind_start:
                ind_end += 1
        nums = nums[:ind_start] + nums[ind_end + 1:]
        # print(nums)
        return len(nums)



sol = Solution()
print(sol.removeElement([0,1,2,2,3,0,4,2], 2))
# print(sol.removeElement([3,2,2,3], 3))