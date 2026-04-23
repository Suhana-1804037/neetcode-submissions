# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def get_length(self, head):
        count = 0
        while head:
            count += 1
            head = head.next
        return count

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        len1 = self.get_length(l1)
        len2 = self.get_length(l2)
        
        if len1<len2:
            l1,l2 = l2,l1
        head = l1
        while l1 and l2:
            l1.val = l1.val + l2.val
            l1 = l1.next
            l2 = l2.next
        l1 = head
        while l1:
            if l1.val>9:
                l1.val = l1.val%10
                if l1.next:
                    l1.next.val += 1
                else:
                    l1.next = ListNode(1)
            l1 = l1.next

        return head













