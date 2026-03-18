# Top K Frequent Elements

# Approach 1 : using hashmap and sorting

def topKFrequent(nums, k):
    counts = {}
    for n in nums:
        counts[n] = counts.get(n,0) + 1

    print("countes : ", counts)

    sorted_items = sorted(counts.items(), key=lambda x: x[1],  reverse=True)

    print("sorted items : ", sorted_items)

    return [item[0] for item in sorted_items[:k]]

# Time = O(nlog n)
# Space = O(n + k)

import heapq

def topKFrequent_heap(nums, k):
    counts = {}
    for n in nums:
        counts[n] = counts.get(n,0) + 1

    heap = []
    for num, freq in counts.items():
        heapq.heappush(heap, (freq, nums))
        if len(heap) > k:
            heapq.heappop(heap)
    
    return [item[1] for item in heap]


if __name__ == "__main__":
    nums = [1,1,2,2,2,3,3,3]
    k = 2
    print("output : ", topKFrequent_heap(nums,k))