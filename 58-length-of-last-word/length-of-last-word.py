class Solution:
    def lengthOfLastWord(self, s):
        s = s.strip()           # Remove trailing and leading spaces
        words = s.split()       # Split by whitespace
        return len(words[-1])   # Return the length of the last word
