# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #Brute Force
        nums = []
        while list1:
            nums.append(list1.val)
            list1 = list1.next
        while list2:
            nums.append(list2.val)
            list2 = list2.next
        
        nums.sort()

        res = ListNode()
        curr = res

        for num in nums:
            curr.next = ListNode(num)
            curr = curr.next

        return res.next