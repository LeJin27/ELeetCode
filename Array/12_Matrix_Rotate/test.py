from main import Solution

testSolution = Solution()

'''
12
34

31
42
'''
matrix = [[1, 2],[3, 4]]
smallSolution = testSolution.matrixShift(matrix)


assert smallSolution == [[3,1], [4, 2]]

