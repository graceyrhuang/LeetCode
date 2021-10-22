from typing import List

def figureUnderGravity(matrix: List[List[int]]) -> List[List[int]]:
	ROW = len(matrix)
	COL = len(matrix[0])

	ff = [['.'] * COL for _ in range(ROW)]

	dist = ROW 
	for c in range(COL):
		bottom = -1
		dists = {}
		for r in range(ROW):
			if matrix[r][c] == 'F':
				bottom =  r

			elif matrix[r][c] == '#' and bottom != -1:
				dist = min(dist, r - bottom - 1)
		dist = min(dist, ROW - bottom - 1)

	
	for r in range(ROW):
		for c in range(COL):
			if matrix[r][c] == 'F':
				ff[r + dist][c] = 'F'
			elif matrix[r][c] == '#':
				ff[r][c] = '#'


	return ff


matrix = [
["F", "F", "F"],
[".", "F", "."],
[".", "F", "F"],
[".", "F", "."],
["F", ".", "."],
[".", ".", "."],
[".", ".", "#"],
[".", ".", "."]
]

print(figureUnderGravity(matrix))