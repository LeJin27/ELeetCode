from main import Solution


testSolution = Solution()


board = [
 ["5","3","9",]
,["6",".",".",]
,[".","9","9"]]

valid = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]




board_row = ["5","3",".",".","7",".",".",".","."]
should_be_valid = testSolution.rowIsValid(board, 0) 
assert should_be_valid== True, "Row should be valid"

should_not_be_valid = testSolution.rowIsValid(board, 2) 
assert should_not_be_valid== False, "Row should not be valid"

should_be_valid = testSolution.columnIsValid(board, 0) 
assert should_be_valid== True, "Column should be valid"

should_not_be_valid = testSolution.columnIsValid(board, 2) 
assert should_not_be_valid== False, "Column should be invalid"

should_be_valid = testSolution.squareIsValid(valid, 6, 6) 
assert should_be_valid == True, "Square should valid"