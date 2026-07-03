# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(0,head)
        p1=temp
        if p1.next==None:
            return head
        p2=head
        if p2.next==None:
            return head
        p3=head.next
        while(p3!=None):
            p2.next=p1
            p1=p2
            p2=p3
            p3=p3.next
        p2.next=p1
        head.next=None
        return p2