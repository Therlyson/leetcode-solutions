#problem 37 leetcode
board = [
	["5", "3", ".", ".", "7", ".", ".", ".", "."],
	["6", ".", ".", "1", "9", "5", ".", ".", "."],
	[".", "9", "8", ".", ".", ".", ".", "6", "."],
	["8", ".", ".", ".", "6", ".", ".", "3", "."],
	["4", ".", ".", "8", ".", "3", ".", ".", "1"],
	["7", ".", ".", ".", "2", ".", ".", ".", "6"],
	[".", "6", ".", ".", ".", ".", "2", "8", "."],
	[".", ".", ".", "4", "1", "9", ".", ".", "5"],
	[".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

lines = [set() for _ in range(9)]
cols  = [set() for _ in range(9)]
subs  = [set() for _ in range(9)]  #números presentes em cada submatriz 3×3

def index_sub(lin, col): #função para mapear cada célula (lin, col) ao índice da sub-grade
    return (lin // 3) * 3 + (col // 3) #lin//3: 0,1,2  → multiplado por 3 desloca aos blocos 0–8

for i in range(9):
    for j in range(9):
        if board[i][j] == '.': 
            continue
        num = int(board[i][j])
        lines[i].add(num)
        cols[j].add(num)
        subs[index_sub(i, j)].add(num)

def can_play(lin, col, num): #“posso jogar num em (lin, col)?”
    return (
        num not in lines[lin]
        and num not in cols[col]
        and num not in subs[index_sub(lin, col)]
    )

def backtracking(lin, col):
    if lin >= 9:
        return True

    # Calcula próximo par (linha, coluna)
    next_lin = lin if col < 8 else lin + 1
    next_col = col + 1 if col < 8 else 0

    # Se a célula já está preenchida, vai direto ao próximo
    if board[lin][col] != '.':
        return backtracking(next_lin, next_col)

    # Senão, tenta todos os dígitos de 1 a 9
    for num in range(1, 10):
        if can_play(lin, col, num):
            board[lin][col] = str(num)
            lines[lin].add(num)
            cols[col].add(num)
            subs[index_sub(lin, col)].add(num)

            # 2) chama recursivamente para a próxima posição
            if backtracking(next_lin, next_col):
                return True    # se encontrou solução completa, propaga sucesso

            # 3) se falhou lá na frente, desfaz a jogada (backtrack)
            board[lin][col] = '.'
            lines[lin].remove(num)
            cols[col].remove(num)
            subs[index_sub(lin, col)].remove(num)

    # Nenhum número serviu aqui → sinaliza falha para o nível anterior
    return False

backtracking(0,0)
print("Solução: ", board)