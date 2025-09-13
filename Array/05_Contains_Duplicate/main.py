class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
      sortedNums = sorted(nums)


      for i in range(1, len(sortedNums)):
        if (sortedNums[i] == sortedNums[i - 1]): 
          return True
      return False
        
  
dog = Solution()

#numList = [2,14,18,22,22]
numList = [1,2,3,1]

print(dog.containsDuplicate(numList))