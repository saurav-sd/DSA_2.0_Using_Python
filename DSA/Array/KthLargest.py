# Kth Largest Element in an Array

# Approach 1 : sort an array

def kthLargest(nums, k):
    nums.sort()
    return nums[-k]

# Time = O(NlogN)
# Space = O(1)

# Heap
import heapq

def KthLargest_heap(nums, k):
    heap = []

    for num in nums:
        heapq.heappush(heap,num)

        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]

# Time = O(n log K)
# Spece = O(N)


if __name__ == "__main__":
    nums = [3,2,1,5,6,4]
    k = 2
    print("output : ", KthLargest_heap(nums, k))