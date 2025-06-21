
def removeDuplicates(nums: list[int]) -> int:
  currentValue = nums[0]
  counter = 1
  for i in range (len(nums) - 1):
    nextValue = nums[i+1]
    if (nextValue != currentValue):
      nums[counter] = nextValue
      currentValue = nextValue
      counter +=1

  return counter

def main():
  nums = [1 ,2 ,2, 3]
  k = removeDuplicates(nums)
  print(k)
  print(nums)


if __name__=="__main__":
    main()