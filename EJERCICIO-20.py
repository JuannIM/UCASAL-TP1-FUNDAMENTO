def esta_ordenada_consecutivamente() -> None:
    """
    Indica si una lista de N números está ordenada consecutivamente en forma ascendente.
    """
    n = int(input("Ingrese la cantidad de números: "))
    if n <= 1:
        print("Se necesitan al menos dos elementos.")
        return

    lista = [int(input(f"Ingrese número {i + 1}: ")) for i in range(n)]

    for i in range(1, n):
        if lista[i] != lista[i - 1] + 1:
            print("La lista no está ordenada consecutivamente ascendente.")
            return

    print("La lista está ordenada consecutivamente ascendente.")


if __name__ == "__main__":
    esta_ordenada_consecutivamente()
