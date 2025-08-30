class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        for i in range(k):
          number= nums.pop(len(nums) - 1)
          nums.insert(0, number)
        
        
  

dog = Solution()
dog.rotate([1,2,3,4], 2)

