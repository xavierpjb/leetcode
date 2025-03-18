# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #create a cycle then break cycle at rotation poin
        # mod by length of list

        if not head:
            return head

        def createCycle():
            temp = head
            lenL = 1
            while temp.next:
                lenL += 1
                temp = temp.next
            temp.next = head
            return lenL
        
        lenL = createCycle()

        k = k % lenL

        dummy = ListNode(0,head)

        temp = dummy
        for _ in range(k):
            temp = temp.next
        head = dummy
        for _ in range(lenL - k):
            head = head.next
            temp = temp.next
        
        temp = head.next
        head.next = None
        
        return temp

        