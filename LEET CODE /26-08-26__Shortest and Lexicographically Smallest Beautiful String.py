class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        ones = []

        for i in range(len(s)):
            if s[i] == '1':
                ones.append(i)

        if len(ones) < k:
            return ""

        ans = ""
        min_len = float('inf')

        for i in range(len(ones) - k + 1):
            start = ones[i]
            end = ones[i + k - 1]

            candidate = s[start:end + 1]
            length = end - start + 1

            if length < min_len or (length == min_len and candidate < ans):
                min_len = length
                ans = candidate

        return ans
