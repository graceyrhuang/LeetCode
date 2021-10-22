
def almostTetris(n:int, m:int, figures:list) -> list:
    grid = [[0] * m for _ in range(n)]

    def fillTetris(index, figure):
        for r in range(n):
            for c in range(m):
                if not grid[r][c] and figure == 1:
                    grid[r][c] = index + 1
                    return

                if ((c + 2) < m
                    and not any(grid[r][c : c + 3])
                    and figure == 2):
                    grid[r][c : c + 3] = [index + 1] * 3
                    return

                if ((c + 1) < m and (r + 1) < n
                    and not any(grid[r][c : c + 2])
                    and not any(grid[r + 1][c : c + 2])
                    and figure == 3):
                    grid[r][c : c + 2] = [index + 1] * 2
                    grid[r + 1][c : c + 2] = [(index + 1)] * 2
                    return

                if ((c + 1) < m and (r + 2) < n
                    and not(grid[r][c] or grid[r + 1][c] or grid[r + 2][c] or grid[r + 1][c + 1])
                	and figure == 4):
                		grid[r][c] = grid[r + 1][c] = grid[r + 2][c] = index + 1
                		grid[r + 1][c + 1] = index + 1
                		return

                if ((c + 2) < m and (r + 1) < n
                    and not (any(grid[r + 1][c : c + 2]) or grid[r][c + 1])
                     and figure == 5):
                    grid[r + 1][c : c + 2] = [(index + 1) for _ in range(3)]
                    grid[r][c + 1] = index + 1
                    return


    for i, figure in enumerate(figures):
        fillTetris(i, figure)
    return grid



n, m = 4, 4
figures = [4, 2, 1, 3]

print(almostTetris(n, m, figures))
