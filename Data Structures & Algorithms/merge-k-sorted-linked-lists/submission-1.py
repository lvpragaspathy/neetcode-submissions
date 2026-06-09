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
            if not list2 or not list1:
                return list2 or list1

            if list2.val < list1.val:
                head = curr = list2
                list2 = list2.next
            else:
                head = curr = list1
                list1 = list1.next

            while list2 and list1:
                if list2.val < list1.val:
                    curr.next = list2
                    list2 = list2.next
                else: 
                    curr.next = list1
                    list1 = list1.next
                curr = curr.next
                
            if list2:
                curr.next = list2
            if list1: 
                curr.next = list1
            
            return head

        for i in range(1, len(lists)):
            lists[i] = mergeTwoLists(lists[i], lists[i - 1])
        
        return lists[-1]



                


                

                




