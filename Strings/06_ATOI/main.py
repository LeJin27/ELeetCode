
class Solution:
    def myAtoi(self, s: str) -> int:
      is_negative = False
      s = s.strip(" ")
      starting_index = 0
      if (s[starting_index] == '-'): 
        is_negative = True
        starting_index += 1
      elif (s[starting_index] == '+'): 
        starting_index += 1

      # checking for 0
      while(starting_index < len(s) - 1 and s[starting_index] == '0'):
        starting_index += 1
      
      ending_index = starting_index
      # checking for is digit

      contains_digit = False


      while(ending_index < len(s) - 1 and s[ending_index].isdigit()):
        ending_index+=1
        if (not s[ending_index].isdigit()):
          ending_index -= 1
          break
        else: 
          contains_digit = True
      
      if (not contains_digit):
        return 0
      
      number_string = s[starting_index: ending_index + 1]

      number_int = int(number_string)
      if (is_negative): 
        number_int *= -1

      int_max = 2147483647
      int_min = -2147483648
      if (number_int > int_max):
        return int_max 
      if (number_int < int_min):
        return int_min
      
      return number_int
      


      
        
test_solution = Solution()
solution = test_solution.myAtoi(" -042")
assert solution == -42

solution = test_solution.myAtoi("1337c0d3")
assert solution == 1337

solution = test_solution.myAtoi("0-1")
assert solution == 0

solution = test_solution.myAtoi("-91283472332")
assert solution ==-2147483648 


solution = test_solution.myAtoi("3.14")
print(solution)
assert solution ==3 