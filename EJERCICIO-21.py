def tipo_de_orden_lista() -> None:
    """
    Indica si una lista de N números está ordenada ascendente, descendente o desordenada.
    """
    n = int(input("Ingrese la cantidad de números: "))
    lista = [int(input(f"Ingrese número {i + 1}: ")) for i in range(n)]

    asc = all(lista[i] <= lista[i + 1] for i in range(n - 1))
    desc = all(lista[i] >= lista[i + 1] for i in range(n - 1))

    if asc:
        print("La lista está ordenada ascendentemente.")
    elif desc:
        print("La lista está ordenada descendentemente.")
    else:
        print("La lista está desordenada.")


if __name__ == "__main__":
    tipo_de_orden_lista()
