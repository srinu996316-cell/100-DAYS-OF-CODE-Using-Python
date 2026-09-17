class Solution(object):

    def minSumOfLengths(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """

        n = len(arr)
        INF = float('inf')

        # best[i] = minimum length of a valid subarray
        # ending at or before index i
        best = [INF] * n

        left = 0
        curr_sum = 0
        ans = INF

        for right in range(n):
            curr_sum += arr[right]

            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1

            if curr_sum == target:
                length = right - left + 1

                # Check for a previous non-overlapping subarray
                if left > 0 and best[left - 1] != INF:
                    ans = min(ans, length + best[left - 1])

                # Store the shortest subarray found so far
                if right == 0:
                    best[right] = length
                else:
                    best[right] = min(best[right - 1], length)

            else:
                if right > 0:
                    best[right] = best[right - 1]

        return -1 if ans == INF else ans
        return -1 if ans == float('inf') else ans
