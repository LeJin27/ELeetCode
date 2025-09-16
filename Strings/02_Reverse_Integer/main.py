class Solution:
    def reverse(self, x: int) -> int:
      s = list(str(x))
      isNegative = False
      if s[0] == '-':
        isNegative = True
      half = int(len(s) / 2)
      for index in range(half):
        right = len(s) - 1 - index
        s[index], s[right] = s[right], s[index]

      if (isNegative):
        del s[-1]
      
      joinedValue = ''.join(s)
      if (isNegative):
        joinedValue = '-' + joinedValue
      
      intValue = int(joinedValue)
      if intValue.bit_length() <= 31:
        return intValue
      else:
        return 0
      
      






      
      


        

test = Solution()
print(test.reverse(1534236469))
