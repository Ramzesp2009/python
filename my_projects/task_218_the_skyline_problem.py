class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        positions = sorted(list(set([x for building in buildings for x in building[:2]])))

        edge_index_map = {x: i for i, x in enumerate(positions)}

        heights = [0] * len(positions)

        for left, right, height in buildings:
            left_idx = edge_index_map[left]
            right_idx = edge_index_map[right]

            for i in range(left_idx, right_idx):
                heights[i] = max(heights[i], height)

        answer = []

        for i in range(len(heights)):
            curr_height = heights[i]
            curr_x = positions[i]

            if not answer or answer[-1][1] != curr_height:
                answer.append([curr_x, curr_height])
        return answer

buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
print(Solution.getSkyline(self, buildings))