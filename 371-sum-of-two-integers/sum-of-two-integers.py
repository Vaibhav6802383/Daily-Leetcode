class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # while b != 0:
        #     c = a & b
        #     a = a ^ b
        #     b = c << 1
        # return a
        return(a+b)