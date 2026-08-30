class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        a = nums.index(min(nums))
        b = nums.index(max(nums))

        left = min(a, b)
        right = max(a, b)

        return min(
            right + 1,
            n - left,
            left + 1 + n - right
        )
