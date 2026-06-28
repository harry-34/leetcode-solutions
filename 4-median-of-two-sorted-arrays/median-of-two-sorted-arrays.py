class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # Ensure nums1 is the smaller array to optimize binary search time to O(log(min(m, n)))
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        total_left = (m + n + 1) // 2
        
        while low <= high:
            # i is the partition index for nums1
            i = (low + high) // 2
            # j is the partition index for nums2
            j = total_left - i
            
            # Handle edge cases where partition falls at the very beginning or end
            A_left = nums1[i - 1] if i > 0 else float('-inf')
            A_right = nums1[i] if i < m else float('inf')
            
            B_left = nums2[j - 1] if j > 0 else float('-inf')
            B_right = nums2[j] if j < n else float('inf')
            
            # Check if we found the correct partition
            if A_left <= B_right and B_left <= A_right:
                # If total length is odd
                if (m + n) % 2 != 0:
                    return max(A_left, B_left)
                # If total length is even
                return (max(A_left, B_left) + min(A_right, B_right)) / 2.0
                
            elif A_left > B_right:
                # i is too big, we need to move the partition left
                high = i - 1
            else:
                # i is too small, we need to move the partition right
                low = i + 1
                
        return 0.0