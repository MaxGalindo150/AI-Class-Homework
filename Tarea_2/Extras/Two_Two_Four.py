import datetime

def is_valid(asignar):
    t = asignar['T']
    w = asignar['W']
    o = asignar['O']
    f = asignar['F']
    u = asignar['U']
    r = asignar['R']

    if t == 0 or f == 0:  # Evitar ceros a la izquierda
        return False

    # Centecimas/Decimas/Unidades
    left_side = t * 100 + w * 10 + o
    right_side = f * 1000 + o * 100 + u * 10 + r
    
    #Ecuacion:
    return left_side + left_side == right_side

def solve_two_two_four():
    letras = ['T', 'W', 'O', 'F', 'U', 'R']
    asignar = {letra: -1 for letra in letras}

    def backtracking(index):
        if index == len(letras):
            if is_valid(asignar):
                return True
            return False

        for digito in range(10):
            if digito in asignar.values():
                continue

            asignar[letras[index]] = digito

            if backtracking(index + 1):
                return True

            asignar[letras[index]] = -1

        return False

    if backtracking(0):
        return asignar
    else:
        return None

start = datetime.datetime.now()
solucion = solve_two_two_four()
end = datetime.datetime.now()



if solucion:
    print(f'Tiempo: {end-start} seg')
    print("Solución encontrada:")
    print(f"T = {solucion['T']}")
    print(f"W = {solucion['W']}")
    print(f"O = {solucion['O']}")
    print(f"F = {solucion['F']}")
    print(f"U = {solucion['U']}")
    print(f"R = {solucion['R']}")
else:
    print("No se encontró una solución.")
