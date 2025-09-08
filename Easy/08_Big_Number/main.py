class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
      lastIndex = len(digits) - 1

      shouldIncrementNext = True

      returningList = []
      for currentIndex in range(lastIndex, -1, -1):
        currentNumber = digits[currentIndex]
        
        if shouldIncrementNext is not False:
          currentNumber += 1

        if (currentNumber - 10 >= 0):
          shouldIncrementNext = True
          currentNumber = 0
        else:
          shouldIncrementNext = False
        
        returningList = [currentNumber] + returningList

      if (shouldIncrementNext is True): 
        returningList = [1] + returningList
      

      return returningList

      

digits = [9]
test = Solution()
print(test.plusOne(digits))


        