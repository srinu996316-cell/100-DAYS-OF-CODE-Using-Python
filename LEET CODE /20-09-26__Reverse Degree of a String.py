class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0

        for i, ch in enumerate(s):
            reverse_value = 26 - (ord(ch) - ord('a'))
            total += reverse_value * (i + 1)

        return total
