class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            for _ in range(n):
                nums1[_] = nums2[_]
            return

        if n == 0:
            return

        nums1_max = nums1[m-1]
        nums2_max = nums2[n-1]
        i = 0
        j = 0

        while m > i and n > j:
            if nums1_max > nums2_max:
                i += 1
                nums1[m + n - i - j] = nums1_max
                # Update nums1_max only if there are remaining elements in nums1
                if i < m:
                    nums1_max = nums1[m - 1 - i]
            else: 
                j += 1
                nums1[m + n - i - j] = nums2_max
                # Update nums2_max only if there are remaining elements in nums2
                if j < n:
                    nums2_max = nums2[n - 1 - j]

        # Handle the remaining elements in nums2
        if n > j:
            for index in range(n - j):
                nums1[index] = nums2[index]
        

        


# Test cases
def test_merge():
    sol = Solution()

    # Test case 1: Standard case
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    sol.merge(nums1, m, nums2, n)
    print("Test Case 1: ", nums1)  # Expected: [1, 2, 2, 3, 5, 6]

    # Test case 2: nums1 is empty
    nums1 = [0, 0, 0]
    m = 0
    nums2 = [1, 2, 3]
    n = 3
    sol.merge(nums1, m, nums2, n)
    print("Test Case 2: ", nums1)  # Expected: [1, 2, 3]

    # Test case 3: nums2 is empty
    nums1 = [1, 2, 3]
    m = 3
    nums2 = []
    n = 0
    sol.merge(nums1, m, nums2, n)
    print("Test Case 3: ", nums1)  # Expected: [1, 2, 3]

    # Test case 5: nums2 is longer than nums1
    nums1 = [1, 0, 0, 0]
    m = 1
    nums2 = [2, 3, 4]
    n = 3
    sol.merge(nums1, m, nums2, n)
    print("Test Case 5: ", nums1)  # Expected: [1, 2, 3, 4]

    # Test case 6: nums1 and nums2 have reverse order
    nums1 = [4, 5, 6, 0, 0, 0]
    m = 3
    nums2 = [1, 2, 3]
    n = 3
    sol.merge(nums1, m, nums2, n)
    print("Test Case 6: ", nums1)  # Expected: [1, 2, 3, 4, 5, 6]

    # Test case 7: Large input case
    nums1 = [i for i in range(500)] + [0] * 500
    m = 500
    nums2 = [i for i in range(500, 1000)]
    n = 500
    sol.merge(nums1, m, nums2, n)
    print("Test Case 7: First 10 elements: ", nums1[:10])  # Expected: [0, 1, 2, ..., 9]
    print("Test Case 7: Last 10 elements: ", nums1[-10:])  # Expected: [990, 991, ..., 999]


test_merge()
        