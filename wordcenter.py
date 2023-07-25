def is_valid_guess(board, word):
    m, n = len(board), len(board[0])
    visited = [[False]*n for _ in range(m)]

    def dfs(i, j, k):
        if k == len(word):
            return True
        if i < 0 or i >= m or j < 0 or j >= n:
            return False
        if visited[i][j] or board[i][j] != word[k]:
            return False
        visited[i][j] = True
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if di == dj == 0:
                    continue
                if dfs(i+di, j+dj, k+1):
                    return True
        visited[i][j] = False
        return False

    for i in range(m):
        for j in range(n):
            if dfs(i, j, 0):
                return True
    return False


board = ["E", "A", "R", "A"], ["N", "L", "E", "C"], [
    "I", "A", "I", "S"], ["B", "Y", "O", "R"]
word = "C"
print(is_valid_guess(board, word))
