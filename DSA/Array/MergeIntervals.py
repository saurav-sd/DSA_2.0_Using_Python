def merge_intervals(intervals):
    if not intervals:
        return []
    
    intervals.sort() # sort by lexographical order default sort
    #intervals.sort(key=lambda x:x[0])

    merged= [intervals[0]]

    for i in range(1,len(intervals)):
        last_end = merged[-1][1]
        curr_start,curr_end = intervals[i]

        if curr_start <= last_end:
            merged[-1][1] = max(curr_end,last_end)
        else:
            merged.append([curr_start,curr_end])

    return merged

# Time = O(nlogn)
# Space = O(n)

if __name__ == "__main__":
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print("Merged intervals : ", merge_intervals(intervals))