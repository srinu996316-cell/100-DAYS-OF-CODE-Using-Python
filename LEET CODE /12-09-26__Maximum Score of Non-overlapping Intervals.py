class Solution(object):
    def maximumWeight(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        n = len(intervals)

        # [left, right, weight, original_index]
        arr = []
        for i in range(n):
            l, r, w = intervals[i]
            arr.append([l, r, w, i])

        arr.sort()

        # Find the next non-overlapping interval
        import bisect
        starts = [x[0] for x in arr]
        nxt = [0] * n

        for i in range(n):
            nxt[i] = bisect.bisect_right(starts, arr[i][1])

        # dp[i][k] = (maximum score, lexicographically smallest indices)
        dp = [[(0, []) for _ in range(5)] for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for k in range(1, 5):

                # Don't take current interval
                skip_score, skip_indices = dp[i + 1][k]

                # Take current interval
                take_score, take_indices = dp[nxt[i]][k - 1]
                take_score += arr[i][2]
                take_indices = sorted(take_indices + [arr[i][3]])

                # Choose better answer
                if take_score > skip_score:
                    dp[i][k] = (take_score, take_indices)
                elif take_score < skip_score:
                    dp[i][k] = (skip_score, skip_indices)
                else:
                    if take_indices < skip_indices:
                        dp[i][k] = (take_score, take_indices)
                    else:
                        dp[i][k] = (skip_score, skip_indices)

        return dp[0][4][1]
