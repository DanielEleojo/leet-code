class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        temp = 0
        for i in range(n-1):
            temp = nums[i] + nums[i+1]
            print(temp)
            nums[i+1] = temp
            
        return nums