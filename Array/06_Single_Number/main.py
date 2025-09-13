class Solution:
  def singleNumber(self, nums: list[int]) -> int:
    containsDuplicate = {}
    for i in range(0, len(nums)):
      currentNum = nums[i]

      if currentNum not in containsDuplicate:
        containsDuplicate[currentNum] = False
      else:
        containsDuplicate[currentNum] = True

      
    for key in containsDuplicate:
      if containsDuplicate[key] == False:
        return key
    
    return 0
      
    



    
    
    


    
dog = Solution()

nums = [4,1,2,1,2]
print(dog.singleNumber(nums))