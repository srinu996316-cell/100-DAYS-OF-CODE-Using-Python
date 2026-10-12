
class Solution(object):
    def maxSum(self, nums, k):
        MOD = 10**9 + 7
        ans = 0
        bits = [0] * 32

        for num in nums:
            for b in range(32):
                if num & (1 << b):
                    bits[b] += 1

        for _ in range(k):
            x = 0
            for b in range(32):
                if bits[b] > 0:
                    x |= (1 << b)
                    bits[b] -= 1

            ans = (ans + x * x) % MOD

        return ans
