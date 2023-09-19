import random

# Definir el tablero del juego de gato como una lista de 9 espacios (3x3)
state = [' ' for _ in range(9)]  # Estado inicial

# Función para imprimir el tablero
def print_state(state):
    for i in range(0, 9, 3):
        print(state[i], '|', state[i + 1], '|', state[i + 2])
        if i < 6:
            print('---------')

# Función para verificar si un jugador está en algún estado terminal
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
            eval = expectimax(state, depth + 1, False)
            state[i] = ' '
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
    return max_eval

def expect_value(state, depth):
    total_eval = 0
    empty_cells = [i for i, value in enumerate(state) if value == ' ']
    probability = 1 / len(empty_cells)

    for i in empty_cells:
        state[i] = 'X'
        total_eval += expectimax(state, depth + 1, True) * probability
        state[i] = ' '

    return total_eval

# Función Expectimax
def expectimax(state, depth, is_maximizing):
    if check_win(state, 'X'):
        return -1
    elif check_win(state, 'O'):
        return 1
    elif is_full(state):
        return 0
    if is_maximizing:
        return max_value(state, depth, float('-inf'), float('inf'))
    else:
        return expect_value(state, depth)

# Función para obtener la mejor jugada para MAX
def get_best_move_MAX(state):
    best_move = -1
    best_eval = float('-inf')
    for i in range(9):
        if state[i] == ' ':
            state[i] = 'O'
            eval = expectimax(state, 0, False)
            state[i] = ' '
            if eval > best_eval:
                best_eval = eval
                best_move = i
    return best_move

# Función para obtener la mejor jugada para MIN
def get_best_move_MIN(state):
    best_move = -1
    best_eval = float('inf')
    for i in range(9):
        if state[i] == ' ':
            state[i] = 'X'
            eval = expectimax(state, 0, True)
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