class Solution(object):

    def numberOfSets(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7

        # Answer = C(n + k - 1, 2 * k)
        N = n + k - 1
        R = 2 * k

        ans = 1

        for i in range(1, R + 1):
            ans = ans * (N - R + i) % MOD
            ans = ans * pow(i, MOD - 2, MOD) % MOD

        return ans
