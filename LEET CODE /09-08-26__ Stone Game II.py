class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        n = len(piles)

        # Suffix sum: suffix[i] = stones from i to end
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        # dp(i, M) = maximum stones current player can get
        # starting from index i with current M
        memo = {}

        def dp(i, M):
            if i >= n:
                return 0

            if (i, M) in memo:
                return memo[(i, M)]

            # If we can take all remaining piles
            if i + 2 * M >= n:
                memo[(i, M)] = suffix[i]
                return suffix[i]

            best = 0

            # Try taking X piles, where 1 <= X <= 2*M
            for X in range(1, 2 * M + 1):
                # Current player gets X piles.
                # Opponent then gets dp(i+X, max(M, X)).
                current = suffix[i] - dp(i + X, max(M, X))
                best = max(best, current)

            memo[(i, M)] = best
            return best

        return dp(0, 1)
