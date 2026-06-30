class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Area = (r - l) * min(heights[l], heights[r])

        # this function returns the area and the index of the min value of l and r.
        def area(l, r, heights):
            if min(heights[l], heights[r]) == heights[l]:
                i = l
            else:
                i = r

            return [(r - l) * heights[i], i]

        max_area = 0
        l = 0
        r = len(heights) - 1


        while l < r:
            curr = area(l, r, heights)
            curr_area = curr[0]
            i = curr[1] # index of the min value of l, r

            if curr_area > max_area:
                max_area = curr_area

            # only move the lesser pointer because we want to use the large value.
            if i == l:
                l += 1
            else:
                r -= 1

        return max_area







