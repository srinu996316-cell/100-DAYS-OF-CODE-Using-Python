class Solution(object):
    def maxPalindromes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = dp[i - 1]

            # Check only substrings of length k and k+1.
            # If a palindrome of length >= k exists,
            # we can always take a palindrome of length k or k+1.
            if i >= k:
                if s[i-k:i] == s[i-k:i][::-1]:
                    dp[i] = max(dp[i], dp[i-k] + 1)

            if i >= k + 1:
                if s[i-k-1:i] == s[i-k-1:i][::-1]:
                    dp[i] = max(dp[i], dp[i-k-1] + 1)

        return dp[n]
