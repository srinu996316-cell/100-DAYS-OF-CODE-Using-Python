class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Find sum of the longest sequential prefix
        total = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                total += nums[i]
            else:
                break

        # Store all numbers in a set
        num_set = set(nums)

        # Find the smallest missing number >= total
        while total in num_set:
            total += 1

        return total
        
