class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """


        counterMax = len(nums)
        counter = 0
        
        while(True):
          if (counter >= counterMax):
            break
          
          currentNum = nums[counter]
          if (currentNum == 0): 
            counterMax -= 1
            nums.pop(counter)
            nums.append(currentNum)
          else: 
            counter += 1



        

test = Solution()

nums = [0,1,0,3,12]
test.moveZeroes(nums)



assert nums == [1,3,12,0,0]

nums = [0]
test.moveZeroes(nums)

assert nums == [0]