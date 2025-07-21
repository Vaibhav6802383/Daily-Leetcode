class Solution(object):
    def numSplits(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        left_counts = [0] * n
        right_counts = [0] * n

        left_set = set()
        for i in range(n):
            left_set.add(s[i])
            left_counts[i] = len(left_set)

        right_set = set()
        for i in range(n - 1, -1, -1):
            right_set.add(s[i])
            right_counts[i] = len(right_set)

        good_splits = 0
        for i in range(n - 1):
            if left_counts[i] == right_counts[i + 1]:
                good_splits += 1

        return good_splits
