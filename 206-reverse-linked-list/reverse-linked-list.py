class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            nextnode = curr.next
            curr.next = prev
            prev = curr
            curr = nextnode
        return prev