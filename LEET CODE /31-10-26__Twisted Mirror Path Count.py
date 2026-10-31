class Solution(object):
    def uniquePaths(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        def move(i, j, direction):
            # Attempt the initial move
            if direction == 0:  # Right
                j += 1
            else:               # Down
                i += 1

            # Continue reflecting until an empty cell is reached
            while 0 <= i < m and 0 <= j < n and grid[i][j] == 1:

                if direction == 0:  # Entered mirror moving right
                    i += 1
                    direction = 1  # Reflect down

                else:              # Entered mirror moving down
                    j += 1
                    direction = 0  # Reflect right

            # Return destination if valid
            if 0 <= i < m and 0 <= j < n:
                return i, j

            return -1, -1

        for i in range(m):
            for j in range(n):

                if dp[i][j] == 0:
                    continue

                # Try moving right
                r, c = move(i, j, 0)

                if r != -1:
                    dp[r][c] = (dp[r][c] + dp[i][j]) % MOD

                # Try moving down
                r, c = move(i, j, 1)

                if r != -1:
                    dp[r][c] = (dp[r][c] + dp[i][j]) % MOD

        return dp[m - 1][n - 1]
