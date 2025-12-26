import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
      string = ''.join(char for char in s if char.isalnum())
      string = string.lower()
      reversed_string = string[::-1]

      return string == reversed_string
      

testSolution = Solution()
s = "A man, a plan, a canal: Panama"
retValue = testSolution.isPalindrome(s)
assert retValue == True

s = "ab_a"
retValue = testSolution.isPalindrome(s)
assert retValue == True
        