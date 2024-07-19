# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        mul = 1 
        while(l1!=None):
            num1 += l1.val * mul
            mul*=10
            l1 = l1.next
        num2 = 0
        mul = 1 
        while(l2!=None):
            num2 += l2.val * mul
            mul*=10
            l2 = l2.next
        
        num1+=num2
        l3 = ListNode()
        h3 = l3
        l3.val = num1%10
        num1//=10
        while num1>0:
            t3 = ListNode()
            t3.val = num1%10
            l3.next = t3
            l3 = t3
            num1//=10
        return h3