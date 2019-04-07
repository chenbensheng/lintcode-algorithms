class SolutionSorted:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        if len(nums) == 1:
            return nums[0]

        if nums[0]<nums[len(nums) - 1]:
            return nums[0]

        left = 0
        right=len(nums) - 1

        while left < right:
            mid = (left + right) / 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]

