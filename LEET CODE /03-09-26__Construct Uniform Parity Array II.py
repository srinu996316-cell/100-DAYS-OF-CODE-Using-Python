class Solution(object):

    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """

        mn = min(nums1)

        # If the minimum element is odd,
        # all elements can be made odd.
        if mn % 2 == 1:
            return True

        # If the minimum is even, check whether
        # all elements are already even.
        for num in nums1:
            if num % 2 == 1:
                return False

        return True
