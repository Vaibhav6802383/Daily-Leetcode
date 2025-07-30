class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        i = 0  # pointer for the place to insert the next unique element

        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]  # replace duplicate with unique

        return i + 1  # number of unique elements
