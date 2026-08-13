# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        if not head.next:
            if head.val == 9:
                head.next = ListNode(val=0, next=None)
                head.val = 1
                return head
            else:
                head.val += 1
                return head


        # first reverse the liked list
        def reverseList(head):
            curr = head
            prev = None

            while curr is not None:
                nextNode = curr.next
                curr.next = prev
                prev = curr
                curr = nextNode

            return prev

        carry = -1
        reversed_head = reverseList(head)
        curr = reversed_head
        while carry != 0:
            curr_val = curr.val
            curr_val += 1

            if curr_val > 9:
                carry = 1
                curr.val = 0
                if not curr.next:
                    curr.next = ListNode(val=1, next=None)
                    break
                curr = curr.next
            else:
                curr.val = curr_val
                carry = 0


        return reverseList(reversed_head)