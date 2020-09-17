# Link to challenge:
# https://www.hackerrank.com/challenges/cavity-map/problem


def cavityMap(grid):
    ceiling = len(grid)

    if ceiling <= 2:
        return grid

    for y in range(1, ceiling - 1):
        for x in range(1, ceiling - 1):
            if (
                    (grid[y - 1][x] == 'X') or
                    (grid[y - 1][x] == 'X') or
                    (grid[y - 1][x] == 'X') or
                    (grid[y - 1][x] == 'X')
            ):
                continue

            if (
                    (grid[y][x]) > (grid[y - 1][x]) and
                    (grid[y][x]) > (grid[y + 1][x]) and
                    (grid[y][x]) > (grid[y][x - 1]) and
                    (grid[y][x]) > (grid[y][x + 1])
            ):
                grid[y] = grid[y][:x] + 'X' + grid[y][x + 1:]

    return grid
