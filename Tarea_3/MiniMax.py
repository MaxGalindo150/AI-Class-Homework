import random

# Definir el tablero del juego de gato como una lista de 9 espacios (3x3)
state = [' ' for _ in range(9)] # Estado incial

# Función para imprimir el tablero
def print_state(state):
    for i in range(0, 9, 3):
        print(state[i], '|', state[i + 1], '|', state[i + 2])
        if i < 6:
            print('---------')

# Función para verificar si un jugador está en algún estado términal
def check_win(state, player):
    win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]  
    for combo in win_combinations:
        if all(state[i] == player for i in combo):
            return True
    return False

# Función para verificar si el tablero está lleno (Estado terminal de empate)
def is_full(state): 
    return ' ' not in state

def max_value(state, depth, alpha, beta):
    max_eval = float('-inf')
    for i in range(9):
        if state[i] == ' ':
            state[i] = 'O'
            eval = minimax(state, depth + 1, False, alpha, beta)
            state[i] = ' '
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
    return max_eval

def min_value(state, depth, alpha, beta):
    min_eval = float('inf')
    for i in range(9):
        if state[i] == ' ':
            state[i] = 'X'
            eval = minimax(state, depth + 1, True, alpha, beta)
            state[i] = ' '
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
    return min_eval


# Función Minimax con poda alfa-beta
def minimax(state, depth, is_maximizing, alpha, beta):
    # Despachador para estados terminales
    if check_win(state, 'X'):
        return -1
    elif check_win(state, 'O'):
        return 1
    elif is_full(state):
        return 0
    # Despachador
    if is_maximizing:
        return max_value(state, depth, alpha, beta)
    else:
        return min_value(state, depth, alpha, beta)

# Función para obtener la mejor jugada para MAX
def get_best_move_MAX(state):
    best_move = -1
    best_eval = float('-inf')
    alpha = float('-inf')
    beta = float('inf')
    for i in range(9):
        if state[i] == ' ':
            state[i] = 'O'
            eval = minimax(state, 0, False, alpha, beta)
            state[i] = ' '
            if eval > best_eval:
                best_eval = eval
                best_move = i
    return best_move

# Función para obtener la mejor jugada para MIN
def get_best_move_MIN(state):
    best_move = -1
    best_eval = float('inf')
    alpha = float('-inf')
    beta = float('inf')
    for i in range(9):
        if state[i] == ' ':
            state[i] = 'X'
            eval = minimax(state, 0, True, alpha, beta)
            state[i] = ' '
            if eval < best_eval:
                best_eval = eval
                best_move = i
    return best_move
flag = True
# Loop principal del juego
while True:
    # Turno de MAX
    print_state(state)
    print("Turno de MAX (O)")
    
    # Modificación para la primera jugada de MAX
    if flag:
        flag = False
        max_move = random.choice([i for i, value in enumerate(state) if value == ' '])
        state[max_move] = 'O'
    else:
        max_move = get_best_move_MAX(state)
        if state[max_move] == ' ':
            state[max_move] = 'O'
    
    if check_win(state, 'O'):
        print_state(state)
        print("MAX ganó")
        break
    elif is_full(state):
        print_state(state)
        print("Empate")
        break
    # Turnos de MIN
    print_state(state)
    print("Turno de MIN (X)")
    min_move = get_best_move_MIN(state)
    if state[min_move] == ' ':
        state[min_move] = 'X'
    else:
        print("¡Esa casilla ya está ocupada!")
        continue

    if check_win(state, 'X'):
        print_state(state)
        print("MIN ganó")
        break
    elif is_full(state):
        print_state(state)
        print("Empate")
        break
    
    