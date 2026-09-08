class Solution(object):

    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        power = 1000

        while power <= n:
            ans += n - power + 1
            power *= 1000

        return ans
