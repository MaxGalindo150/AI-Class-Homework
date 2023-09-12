import datetime
start = datetime.datetime.now()
class NQueens_Backtracking:

    def __init__(self, N):
        self.N = N  # Tamaño del tablero N x N
        self.board = [-1] * N  # Utilizamos un solo array para almacenar las filas de las reinas en cada columna
        self.safe_rows = set()
        self.diagonal_asc = set()
        self.diagonal_desc = set()

    def is_safe(self, row, col):
        # Verifica si es seguro colocar una reina en la posición (row, col)
        if row in self.safe_rows or col + row in self.diagonal_asc or col - row in self.diagonal_desc:
            return False
        return True

    def solve(self, col):
        if col >= self.N:
            return True
        for row in range(self.N):
            if self.is_safe(row, col):
                self.board[col] = row
                self.safe_rows.add(row)
                self.diagonal_asc.add(col + row)
                self.diagonal_desc.add(col - row)
                if self.solve(col + 1):
                    return True
                self.safe_rows.remove(row)
                self.diagonal_asc.remove(col + row)
                self.diagonal_desc.remove(col - row)
        return False

    def display(self):
        for row in self.board:
            line = ["Q" if i == row else "." for i in range(self.N)]
            print(" ".join(line))

N = 8
n_queens_problem = NQueens_Backtracking(N)

end = datetime.datetime.now()

total_time = end - start

if n_queens_problem.solve(0):
    print(f'Tiempo: {total_time} seg')
    print(f"Solución para {N} reinas:")
    n_queens_problem.display()
else:
    print("No se encontró solución.")
        


