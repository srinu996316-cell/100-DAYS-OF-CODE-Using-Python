class Solution(object):
    def sumGame(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        diff = 0
        q = 0

        for i in range(n):
            if num[i] == '?':
                if i < n // 2:
                    q += 1
                else:
                    q -= 1
            else:
                if i < n // 2:
                    diff += int(num[i])
                else:
                    diff -= int(num[i])

        return diff * 2 != -9 * q
