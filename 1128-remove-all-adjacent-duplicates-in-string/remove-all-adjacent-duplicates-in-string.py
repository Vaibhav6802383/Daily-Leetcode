class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for char in s:
            if stack and stack[-1] == char:
                stack.pop()  # remove the duplicate pair
            else:
                stack.append(char)  # add character to stack

        return ''.join(stack)
