def insert_interval(intervals, new_interval):
    result = []
    for interval in intervals:
        # Case 1: No overlap, and current interval ends before the new interval starts
        if interval[1] < new_interval[0]:
            result.append(interval)
        # Case 2: No overlap, and current interval starts after the new interval ends
        elif interval[0] > new_interval[1]:
            result.append(new_interval)
            new_interval = interval  # Shift new_interval to process remaining intervals
        # Case 3: Overlapping intervals
        else:
            new_interval[0] = min(new_interval[0], interval[0])
            new_interval[1] = max(new_interval[1], interval[1])
    # Add the final merged interval
    result.append(new_interval)
    return result

intervals = [[1, 3], [6, 9]]
new_interval = [2,5]


print(insert_interval(intervals, new_interval))
