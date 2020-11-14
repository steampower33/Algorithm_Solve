sudoku = [list(map(int, input().split())) for _ in range(9)]
zeros = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]

isDone = False

def isHopeful(i, j):
    Hopeful = [i for i in range(1, 10)]

    for k in range(9):
        if sudoku[i][k] in Hopeful:
            Hopeful.remove(sudoku[i][k])
        if sudoku[k][j] in Hopeful:
            Hopeful.remove(sudoku[k][j])

    i //= 3
    j //= 3
    for p in range(i * 3, (i + 1) * 3):
        for q in range(j * 3, (j + 1) * 3):
            if sudoku[p][q] in Hopeful:
                Hopeful.remove(sudoku[p][q])

    return Hopeful

def dfs(x):
    global isDone
    if isDone:
        return

    if x == len(zeros):
        for row in sudoku:
            print(*row)
        isDone = True
        return

    else:
        (i, j) = zeros[x]
        hopeful = isHopeful(i, j)

        for hope in hopeful:
            sudoku[i][j] = hope
            dfs(x+1)
            sudoku[i][j] = 0

dfs(0)