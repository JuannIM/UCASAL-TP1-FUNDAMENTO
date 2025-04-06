def esta_ordenada_ascendentemente() -> None:
    """
    Dada una lista de N números, indica si está ordenada ascendentemente.
    """
    n = int(input("Ingrese la cantidad de números: "))
    lista = [int(input(f"Ingrese número {i + 1}: ")) for i in range(n)]

    for i in range(1, n):
        if lista[i] < lista[i - 1]:
            print("La lista no está ordenada ascendentemente.")
            return

    print("La lista está ordenada ascendentemente.")


if __name__ == "__main__":
    esta_ordenada_ascendentemente()
