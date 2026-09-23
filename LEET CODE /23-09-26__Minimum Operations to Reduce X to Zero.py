class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        
        total = sum(nums)
        target = total - x
        
        # If target is negative, impossible
        if target < 0:
            return -1
        
        # We need to find the longest subarray
        # whose sum is equal to target.
        left = 0
        curr_sum = 0
        max_len = -1
        
        for right in range(len(nums)):
            curr_sum += nums[right]
            
            # Shrink window if sum becomes too large
            while left <= right and curr_sum > target:
                curr_sum -= nums[left]
                left += 1
            
            # Found a subarray with required sum
            if curr_sum == target:
                max_len = max(max_len, right - left + 1)
        
        # No valid subarray found
        if max_len == -1:
            return -1
        
        return len(nums) - max_len
