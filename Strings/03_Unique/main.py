class Solution:
    def firstUniqChar(self, s: str) -> int:
      sList = list(s)
      sDict = {}

      for index, value in enumerate(sList):
        keyExists = sDict.get(value, None)
        if (keyExists is not None):
          # unqique is true
          sDict[value] = False
        else: 
          sDict[value] = index

      for _, key in enumerate(sDict):
        if sDict[key] is not False:
          return sDict[key]
          



      return -1;
        
test = Solution()
returnCode = test.firstUniqChar('leetcode')

assert returnCode == 0

returnCode = test.firstUniqChar('loveleetcode')
assert returnCode == 2

returnCode = test.firstUniqChar('aabb')
assert returnCode == -1