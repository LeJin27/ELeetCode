
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:


      biggestLen = len(nums1)
      if len(nums2) > len(nums1):
        biggestLen = len(nums2) 

      dictNums1 = {}
      dictNums2 = {}
      for i in range(0, biggestLen):
        currentPlus = nums1[i] if len(nums1) > i else False
        currentMinus = nums2[i] if len(nums2) > i else False

        # get count of num 1
        if (currentPlus is not False):
          key = dictNums1.get(currentPlus)
          print(key)
          if (key == None):
            dictNums1[currentPlus] = 1
          else: 
            dictNums1[currentPlus] += 1

        # get count of num 2
        if (currentMinus is not False):
          key = dictNums2.get(currentMinus)
          if (key == None):
            dictNums2[currentMinus] = 1
          else: 
            dictNums2[currentMinus] += 1
      
      
      returnedList = []

      print(dictNums1)
      print(dictNums2)
      for key in dictNums1:
        if dictNums2.get(key) != None:
          intersectCount = dictNums1[key]
          if dictNums2[key] < dictNums1[key]:
            intersectCount = dictNums2[key]

          print(intersectCount)

          for i in range(0, intersectCount):
            returnedList.append(key)


      



      return returnedList
        

dog = Solution()


nums1 = [8, 0, 3]
nums2 = [0, 0]
print(dog.intersect(nums1, nums2))