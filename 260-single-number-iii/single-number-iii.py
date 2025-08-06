class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0
        for num in nums:
            xor ^= num

        diff = xor & -xor

        x = 0
        for num in nums:
            if num & diff:
                x ^= num

        return [x, xor ^ x]
