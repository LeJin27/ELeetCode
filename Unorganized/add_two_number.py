from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self) -> str:
      recBuildString = ""
      nextValue = self.next;
      # base case
      if (nextValue == None):
        recBuildString += str(self.val)
      else:
        recBuildString += str(listNodeToInt(self.next))
        recBuildString += str(self.val)
  
      return recBuildString
    
def listNodeToInt(node, recBuildString = "") -> int:
  nextValue = node.next;
  # base case
  if (nextValue == None):
    recBuildString += str(node.val)
  else:
    recBuildString += str(listNodeToInt(node.next))
    recBuildString += str(node.val)
  linkedListValue = int(recBuildString)
  return linkedListValue

def intToListNode(value: int) -> ListNode | None:
  # 807 => [7. 0, 8]
  strValue = str(value)
  intMapping = list(map(int, strValue))


  currentNode = None
  for i in intMapping:
    if (currentNode != None):
      nextNode = ListNode(currentNode.val, currentNode.next)
    else: 
      nextNode = None
    
    currentNode = ListNode(i, currentNode)
  
  return currentNode


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
      value_1 = listNodeToInt(l1)
      value_2 = listNodeToInt(l2)
      sumValue = value_1 + value_2
      newList = intToListNode(sumValue)

      return  newList
  

if __name__ == "__main__":



  p1 = ListNode(2, ListNode(4, ListNode(3)))
  p2 = ListNode(5, ListNode(6, ListNode(4)))
  #print(getLinkedListValue(p2))
  #print(getLinkedListValue(p1))

  print(intToListNode(807))






#convertIntToLinked(4)
