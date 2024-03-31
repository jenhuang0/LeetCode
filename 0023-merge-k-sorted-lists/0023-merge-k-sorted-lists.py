# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #defaultdict for counting occurences
        count = defaultdict(int)

        for l in lists:
            while l:
                count[l.val] +=1
                l = l.next
        
        #sort the dict keys
        sorted_keys = sorted(count.keys())

        #create a new sorted ll
        dummy = ListNode(None)
        current = dummy

        for key in sorted_keys:
            counter = count[key]
            while counter > 0:
                current.next = ListNode(key)
                current = current.next
                counter -= 1
        return dummy.next