class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = current = ListNode(0)
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # divmod returns both (quotient, remainder) at the same time
            carry, val = divmod(v1 + v2 + carry, 10)
            
            current.next = ListNode(val)
            current = current.next

            # Advance pointers cleanly
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next