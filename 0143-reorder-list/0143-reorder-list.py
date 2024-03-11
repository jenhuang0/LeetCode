# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #reverse second list
        second = slow.next
        slow.next = None #cut the link
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        #merge two
        second = prev
        first= head
        while second:
            temp1 =first.next
            temp2 =second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
        
        