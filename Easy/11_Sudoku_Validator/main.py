class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
      for i in range(0, 9):
        if self.rowIsValid(board, i) is False:
          print("here")
          return False
        if self.columnIsValid(board, i) is False:
          print("here")
          return False
      
      for x in range(0, 3):
        for y in range(0, 3):
          if self.squareIsValid(board, 3*x, 3*y) is False:
            print(3* x, 3* y)
            return False

      return True

    def rowIsValid(self, board: list[list[str]], rowIndex: int) -> bool:
      rowDict = {}

      boardRow = board[rowIndex]
      for _, key in enumerate(boardRow):
        if key != ".":
          if (key not in rowDict):
            rowDict[key] = True
          else: 
            return False
      return True

    def columnIsValid(self, board: list[list[str]], columnIndex: int) -> bool:
      rowDict = {}

      for _, row in enumerate(board):
        key = row[columnIndex]
        if key != ".":
          if (key not in rowDict):
            rowDict[key] = True
          else: 
            return False
      return True
    
    def squareIsValid(self, board: list[list[str]], rowIndex, columnIndex) -> bool:
      rowDict = {}

      for _, row in enumerate(board[rowIndex:rowIndex+3], start=rowIndex):
        for _, key in enumerate(row[columnIndex: columnIndex+3], start=columnIndex):
          if key != ".":
            if (key not in rowDict):
              rowDict[key] = True
            else: 
              return False
      return True
      

        
      

if __name__ == '__main__':
  testSolution = Solution()

  board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]




  result = testSolution.isValidSudoku(board)
  print("-----------Solution------------")
  print(result)
  assert result == True


        

  invalidBoard = [["8","3",".",".","7",".",".",".","."]
  ,["6",".",".","1","9","5",".",".","."]
  ,[".","9","8",".",".",".",".","6","."]
  ,["8",".",".",".","6",".",".",".","3"]
  ,["4",".",".","8",".","3",".",".","1"]
  ,["7",".",".",".","2",".",".",".","6"]
  ,[".","6",".",".",".",".","2","8","."]
  ,[".",".",".","4","1","9",".",".","5"]
  ,[".",".",".",".","8",".",".","7","9"]]
  result = testSolution.isValidSudoku(invalidBoard)
  print(result)
  assert result == False