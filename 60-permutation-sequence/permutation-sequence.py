import math

class Solution:
    def getPermutation(self, n, k):
        numbers = [str(i) for i in range(1, n+1)]
        k -= 1  # Convert to 0-based index
        result = ""

        for i in range(n, 0, -1):
            fact = math.factorial(i - 1)
            index = k // fact
            result += numbers.pop(index)
            k %= fact

        return result
