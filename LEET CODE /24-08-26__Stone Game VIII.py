class Solution(object):
    def stoneGameVIII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        n = len(stones)

        # Calculate prefix sums
        prefix = [0] * n
        prefix[0] = stones[0]

        for i in range(1, n):
            prefix[i] = prefix[i - 1] + stones[i]

        # Start with taking all stones
        ans = prefix[-1]

        # Try every possible split
        for i in range(n - 2, 0, -1):
            ans = max(ans, prefix[i] - ans)

        return ans
