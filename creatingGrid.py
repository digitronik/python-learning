g = [['.', '.', '.', '.', '.', '.'],
       ['.', 'O', 'O', '.', '.', '.'],
       ['O', 'O', 'O', 'O', '.', '.'],
       [',', 'O', 'O', 'O', 'O', '.'],
       ['.', 'O', 'O', 'O', 'O', 'O'],
       [',', 'O', 'O', 'O', 'O', '.'],
       ['O', 'O', 'O', 'O', '.', '.'],
       ['.', 'O', 'O', '.', '.', '.'],
       ['.', '.', '.', '.', '.', '.']]
def grid(g):
    rows = len(g)  
    colm = len(g[0])  
    for j in range(colm):
        print()
        for i in range(rows):
            print(g[i][j],end='*')
grid(g)