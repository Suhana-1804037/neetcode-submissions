# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lng, cnt = 0, 0
        curr = head
        while curr:
            lng+=1
            curr = curr.next
        lng = lng - n +1
        if lng == 1:
            return head.next
        curr = head
        while curr:
            cnt+=1
            if cnt+1==lng:
                p = curr.next.next
                curr.next = p
                break
            curr = curr.next
        return head