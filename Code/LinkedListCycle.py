# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        dictval={}
        curNode = head
        try:
            while curNode.next is not None:
                try:
                    dictval[curNode.next]+=1
                except:
                    dictval[curNode.next]=1
                if(dictval[curNode.next]>1):
                    return True
                curNode = curNode.next
            return False
        except:
            return False
            
