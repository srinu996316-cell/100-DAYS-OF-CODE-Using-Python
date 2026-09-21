class Solution(object):
    def resultArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = [0] * k
        dp = [0] * k

        for num in nums:
            x = num % k
            new_dp = [0] * k

            # Start a new subarray
            new_dp[x] += 1

            # Extend previous subarrays
            for r in range(k):
                if dp[r]:
                    new_r = (r * x) % k
                    new_dp[new_r] += dp[r]

            # Add all subarrays ending here
            for r in range(k):
                ans[r] += new_dp[r]

            dp = new_dp

        return ans
