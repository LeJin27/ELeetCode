class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        half = int(len(s) / 2)
        for index in range(half):
          right = len(s) - 1 - index
          s[index], s[right] = s[right], s[index]



          
  
testSolution = Solution()
s = ['d', 'o', 'g']
testSolution.reverseString(s)

print(s)

        