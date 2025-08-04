import heapq

class Solution:
    def mergeKLists(self, lists):
        heap = []
        for i, node in enumerate(lists):
            if node:
                # Push (value, index, node) to avoid comparison error
                heapq.heappush(heap, (node.val, i, node))
        
        dummy = ListNode()
        current = dummy

        while heap:
            val, i, node = heapq.heappop(heap)
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next
