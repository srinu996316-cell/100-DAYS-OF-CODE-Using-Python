class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: List[int]
        """

        pairs = sorted((num, i) for i, num in enumerate(nums))
        ans = nums[:]
        n = len(nums)
        start = 0

        while start < n:
            end = start

            # Find connected group
            while end + 1 < n and pairs[end + 1][0] - pairs[end][0] <= limit:
                end += 1

            # Get indices and values of the group
            indices = sorted(pairs[i][1] for i in range(start, end + 1))
            values = [pairs[i][0] for i in range(start, end + 1)]

            # Put smallest values at smallest indices
            for index, value in zip(indices, values):
                ans[index] = value

            start = end + 1

        return ans
        
