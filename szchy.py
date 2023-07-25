def knight(start, end):

    start_col = ord(start[0]) - ord('a')
    start_row = int(start[1]) - 1
    end_col = ord(end[0]) - ord('a')
    end_row = int(end[1]) - 1

    if start_col == end_col and start_row == end_row:
        return 0

    if start_col < 0 or start_col > 7 or start_row < 0 or start_row > 7:
        return -1
    if end_col < 0 or end_col > 7 or end_row < 0 or end_row > 7:
        return -1

    if (abs(start_col - end_col) == 1 and abs(start_row - end_row) == 2) or \
       (abs(start_col - end_col) == 2 and abs(start_row - end_row) == 1):
        return 1

    queue = [(start_col, start_row, 0)]
    visited = set()
    while queue:
        col, row, moves = queue.pop(0)
        if col == end_col and row == end_row:
            return moves
        if (col, row) in visited:
            continue
        visited.add((col, row))
        for d_col, d_row in [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]:
            new_col = col + d_col
            new_row = row + d_row
            if 0 <= new_col <= 7 and 0 <= new_row <= 7:
                queue.append((new_col, new_row, moves + 1))
    return -1
arr = [['a1', 'c1', 2], ['a1', 'f1', 3], ['a1', 'f3', 3], ['a1', 'f4', 4], ['a1', 'f7', 5]]
for x in arr:
    z = knight(x[0], x[1])
    print(z)