class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        seen = set(nums)
        multiple = k

        while multiple in seen:
            multiple += k

        return multiple
