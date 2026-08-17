class Solution(object):
    def stoneGameV(self, stoneValue):
        n = len(stoneValue)
        pre = [0] * (n + 1)

        for i in range(n):
            pre[i + 1] = pre[i] + stoneValue[i]

        dp = [[-1] * n for _ in range(n)]

        def solve(i, j):
            if i == j:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            ans = 0
            left = 0
            right = pre[j + 1] - pre[i]

            for k in range(i, j):
                left += stoneValue[k]
                right -= stoneValue[k]

                if left < right:
                    if ans < 2 * left:
                        ans = max(ans, left + solve(i, k))

                elif left > right:
                    if ans < 2 * right:
                        ans = max(ans, right + solve(k + 1, j))
                    else:
                        break

                else:
                    ans = max(ans,
                              left + solve(i, k),
                              right + solve(k + 1, j))

            dp[i][j] = ans
            return ans

        return solve(0, n - 1)
