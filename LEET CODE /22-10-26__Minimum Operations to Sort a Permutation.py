class Solution(object):
    def minOperations(self, nums):
        n = len(nums)
        p = nums.index(0)
        best = float("inf")

        # Form 1: rotate left p times sorts the array.
        if nums[p:] + nums[:p] == list(range(n)):
            best = min(best, p, n - p + 2)

        # Form 2: reverse, then rotate left m times sorts the array.
        rev = nums[::-1]
        m = n - 1 - p
        if rev[m:] + rev[:m] == list(range(n)):
            best = min(best, min(m, n - m) + 1)

        return -1 if best == float("inf") else best
