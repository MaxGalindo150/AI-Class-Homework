#Este codigo resuelve Sudoku con Bacitraciing
import datetime
tablero = [
    [0, 2, 0, 0, 8, 9, 0, 4, 7],
    [0, 0, 9, 7, 0, 4, 0, 0, 0],
    [0, 6, 4, 0, 0, 0, 9, 0, 8],
    [0, 5, 3, 9, 7, 8, 0, 0, 6],
    [0, 0, 6, 0, 4, 0, 7, 9, 0],
    [0, 0, 7, 0, 3, 0, 2, 0, 5],
    [6, 0, 1, 5, 9, 0, 8, 2, 4],
    [5, 0, 2, 8, 0, 6, 3, 0, 9],
    [0, 3, 8, 0, 0, 7, 5, 6, 1]
]

def is_valid(tablero, r, c, i):
    
    #Verificar fila
    row_safe = i not in tablero[r]
    
    #Verificar Columna
    column_safe = i not in [tablero[i][c] for i in range(9)]
    
    #Verificar grid de 3x3
    grid_safe = i not in [tablero[i][j] for i in range(r//3*3, r//3*3+3) for j in range(c//3*3, c//3*3+3)]

    return row_safe and column_safe and grid_safe


def solve(tablero, row=0, col=0):
    
    # Caso base: si row llega a 9, hemos resuelto 
    if row == 9:
        return True
    
    # Si hemos completado una fila, pasamos a la siguiente fila (row) y reiniciamos la columna (col) a 0
    elif col == 9:
        return solve(tablero, row+1, 0)
    
    # Si la celda actual ya contiene un número (no es 0), pasamos a la siguiente columna
    elif tablero[row][col] != 0:
        return solve(tablero, row, col+1)
    else:
        
        # Si la celda actual está vacia (0), probamos números del 1 al 9
        for i in range(1, 10):
            
            # Comprobamos si el número i es válido en la celda actual
            if is_valid(tablero, row, col, i):
                
                # Si es válido, asignamos i a la celda y continuamos resolviendo el resto del tablero
                tablero[row][col] = i
                
                # Llamamos recursivamente a solve para la siguiente columna
                if solve(tablero, row, col+1):
                    return True  # Si la solución es exitosa, retornamos True
                
                # Si la solución no es exitosa, deshacemos la asignación y probamos con otro número
                tablero[row][col] = 0
        
        # Si ningún número es válido en esta celda, retornamos False para retroceder y probar otra ruta
        return False
    
# Resolver el Sudoiu
start = datetime.datetime.now()
solve(tablero)
end = datetime.datetime.now()

# Imprimir el tablero resuelto
print(f'Tiempo: {end-start} seg')
print(*tablero, sep='\n')