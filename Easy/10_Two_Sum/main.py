class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
      numDict = {}
      for index in range(0, len(nums)):
        numberKey = nums[index]
        numDict[numberKey] = index 

      








      
      



      

      return []

      
      
  
solutionTest = Solution()

#nums = [2,7,11,15]
#target = 9
#twoSum = solutionTest.twoSum(nums, target)
#assert twoSum == [0,1]

nums = [3, 2, 4]
target = 6
twoSum = solutionTest.twoSum(nums, target)
assert twoSum == [1,2]

        
nums = [3, 3]
target = 6
twoSum = solutionTest.twoSum(nums, target)
assert twoSum == [0,1]