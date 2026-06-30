class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Returns the area and the index of the min value of l and r.
        def area(l, r, heights):
            if min(heights[l], heights[r]) == heights[l]:
                i = l
            else:
                i = r

            # Area = (r - l) * min(heights[l], heights[r])
            return (r - l) * heights[i], i

        max_area, l, r = 0, 0, len(heights) - 1
        
        while l < r:
            curr_area, index_min = area(l, r, heights)
            max_area = max(curr_area, max_area)

            # only move the lesser pointer because we want to use the large value.
            if index_min == l:
                l += 1
            else:
                r -= 1

        return max_area







