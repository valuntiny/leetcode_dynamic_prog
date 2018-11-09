'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
'''


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0

        localSum = maxSum = float('-inf')
        for i in nums:
            localSum = max(localSum + i, i)
            maxSum = max(maxSum, localSum)

        return maxSum