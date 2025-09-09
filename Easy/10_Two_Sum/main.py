class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_dict = {}
        for index, value in enumerate(nums):

            if value in num_dict.keys():
              num_dict[value].append(index)
            else:
              num_dict[value] = [index]


        for index, key in enumerate(num_dict):
          first_return_value = num_dict[key]
          target_difference_key = target - key

          # now need to find the target diference index
          possible_second_return_value = num_dict.get(target_difference_key, None)
          if (possible_second_return_value is not None):
            # conditional check if same value
            if (possible_second_return_value == first_return_value ):
              if len(first_return_value) > 1:
                return [first_return_value[0], possible_second_return_value[1]]
            else: 
              return [first_return_value[0], possible_second_return_value[0]]





        return []


solutionTest = Solution()

#nums = [2,5,5,11] 
#target = 10
#twoSum = solutionTest.twoSum(nums, target)
#assert twoSum == [0,1]


nums = [3, 2, 4]
target = 6
twoSum = solutionTest.twoSum(nums, target)
assert twoSum == [1, 2]


nums = [3, 3]
target = 6
twoSum = solutionTest.twoSum(nums, target)
assert twoSum == [0, 1]
