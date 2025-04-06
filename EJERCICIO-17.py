def hay_repetidos_en_ordenada() -> None:
    """
    Dada una lista ordenada de N números, indica si hay elementos repetidos.
    """
    n = int(input("Ingrese la cantidad de números: "))
    if n <= 1:
        print("Se necesitan al menos dos elementos.")
        return

    lista = []
    for i in range(n):
        num = int(input(f"Ingrese el número {i + 1}: "))
        lista.append(num)

    for i in range(1, n):
        if lista[i] == lista[i - 1]:
            print("Hay elementos repetidos.")
            return

    print("No hay elementos repetidos.")


if __name__ == "__main__":
    hay_repetidos_en_ordenada()
