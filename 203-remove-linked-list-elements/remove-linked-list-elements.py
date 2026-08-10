# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dumHead = ListNode(-1)
        dumHead.next = head

        curr = dumHead
        while curr.next != None:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dumHead.next