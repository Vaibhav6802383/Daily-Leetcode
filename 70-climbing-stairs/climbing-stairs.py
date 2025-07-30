class Solution:
    def climbStairs(self, n):
        if n <= 2:
            return n

        a, b = 1, 2  # base cases for n = 1 and n = 2

        for _ in range(3, n + 1):
            a, b = b, a + b  # Fibonacci update

        return b
