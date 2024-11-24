class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # Step 1: Sort intervals by start time
        intervals.sort(key=lambda x: x[0])  # Timsort with O(n log n)

        # Step 2: Merge intervals
        merged = []
        for interval in intervals:
            # If the list of merged intervals is empty or there is no overlap
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Overlapping intervals, merge them
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
    



solution = Solution()

# Test cases
test_cases = [
    [[1, 3], [2, 6], [8, 10], [15, 18]],
    [[1, 4], [4, 5]],
    [[1, 2], [3, 4], [5, 6]],
    [[1, 10]],
    [],
    [[1, 10], [2, 6], [3, 5]],
    [[1, 4], [5, 6], [3, 5]],
    [[8, 10], [1, 3], [2, 6], [15, 18]],
    [[1, 5], [2, 6], [3, 7], [4, 8]],
]

# Run and display results
for intervals in test_cases:
    print(f"Input: {intervals}")
    print(f"Output: {solution.merge(intervals)}")
    print()