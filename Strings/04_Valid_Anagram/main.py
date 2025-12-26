class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      dictAna = {}

      for _, value in enumerate(s):
        if (value not in dictAna): 
          dictAna[value] = 1
        else:
          dictAna[value] += 1

      for _, value in enumerate(t):
        if (value not in dictAna): 
          return False
        else:
          dictAna[value] -= 1
      
      return (all(value == 0 for value in dictAna.values()))


      


testSolution = Solution()
      
s = "anagram"
t = "nagaram"
solution = testSolution.isAnagram(s, t)

assert solution == True

print(solution)


        