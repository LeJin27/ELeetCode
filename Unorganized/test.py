from add_two_number import ListNode
from add_two_number import Solution

def listNodeCanConvertToStringTest():
  correctString = "342"
  p1 = ListNode(2, ListNode(4, ListNode(3)))
  p1String = str(p1)
  assert(correctString == p1String)

def listNodeCanAddTest():
  p1 = ListNode(2, ListNode(4, ListNode(3)))
  p2 = ListNode(5, ListNode(6, ListNode(4)))
  solution = Solution()
  sumListNode = solution.addTwoNumbers(p1, p2)
  strSum = str(sumListNode)

  assert(strSum == "807")






  
  
  





if __name__ == "__main__":
  listNodeCanConvertToStringTest()

  listNodeCanAddTest()