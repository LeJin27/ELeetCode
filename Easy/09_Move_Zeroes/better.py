class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        index = 0
        nonZeroIndex = 0

        # Rather than moving the zeroes we move the numbers instead
        while index < len(nums):
          if nums[index] != 0:
            tempValue = nums[index]
            nums[index] = nums[nonZeroIndex]
            nums[nonZeroIndex] = tempValue
            nonZeroIndex += 1
          
          index += 1







        

test = Solution()

nums = [0,1,0,3,12]
test.moveZeroes(nums)



assert nums == [1,3,12,0,0]

nums = [0]
test.moveZeroes(nums)

assert nums == [0]