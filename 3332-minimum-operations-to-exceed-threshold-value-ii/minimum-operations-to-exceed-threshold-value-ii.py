class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)  # Convert the list into a min-heap
        c = 0
        
        while len(nums) > 1 and nums[0] < k:
            x = heapq.heappop(nums)  # Extract smallest element
            y = heapq.heappop(nums)  # Extract second smallest element
            val = min(x, y) * 2 + max(x, y)  # Apply the given operation
            heapq.heappush(nums,val)  # Add the new value back to the heap
            c += 1  # Increment operation count
        return c