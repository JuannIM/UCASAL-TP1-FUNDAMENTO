from itertools import permutations

def mayor_numero_con_digitos() -> None:
    """
    Dados 3 dígitos, genera y muestra el mayor número que se puede formar con ellos.
    """
    print("Ingrese tres dígitos (0-9):")
    digitos = []
    for i in range(3):
        d = input(f"Dígito {i + 1}: ")
        if not d.isdigit() or not (0 <= int(d) <= 9):
            print("Debe ingresar dígitos válidos (0-9).")
            return
        digitos.append(d)

    combinaciones = [''.join(p) for p in permutations(digitos)]
    mayor = max(int(num) for num in combinaciones)
    print(f"El mayor número posible es: {mayor}")


if __name__ == "__main__":
    mayor_numero_con_digitos()
