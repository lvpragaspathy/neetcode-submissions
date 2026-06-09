# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or lists == [[]]:
            return None

        if len(lists) == 1:
            return lists[0]
            
        def mergeTwoLists(list2, list1): 
            head = ListNode()

            if list2.val < list1.val:
                head.val = list2.val
                list2 = list2.next
            else:
                head.val = list1.val
                list1 = list1.next

            curr = head

            while list2 and list1:
                if list2.val < list1.val:
                    curr.next = ListNode(val=list2.val)
                    curr = curr.next
                    list2 = list2.next
                else: 
                    curr.next = ListNode(val=list1.val)
                    curr = curr.next
                    list1 = list1.next
                
            if list2:
                curr.next = list2
            if list1: 
                curr.next = list1
            
            return head

        for i in range(1, len(lists)):
            lists[i] = mergeTwoLists(lists[i], lists[i - 1])
        
        return lists[-1]


                


                

                




