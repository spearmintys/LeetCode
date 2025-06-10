# Sort intervals by start time
# Initialize result with the first interval
# For each interval:
    # If it overlaps with the last in result:
        # Merge them by updating the end
    # Else:
        # Append it to result
# Return result



class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        # Step 1: sort intervals by start
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]

        # Step 2: go through and merge
        for current in intervals[1:]:
            last = merged[-1]
            if current[0] <= last[1]:  # overlap
                last[1] = max(last[1], current[1])
            else:
                merged.append(current)

        return merged