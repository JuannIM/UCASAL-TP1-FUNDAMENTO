def mayor_de_a_en_b() -> None:
    """
    Dadas dos listas A y B, indica si el mayor de A se encuentra en B.
    """
    n_a = int(input("Ingrese la cantidad de números en la lista A: "))
    lista_a = [int(input(f"A[{i + 1}]: ")) for i in range(n_a)]

    n_b = int(input("Ingrese la cantidad de números en la lista B: "))
    lista_b = [int(input(f"B[{i + 1}]: ")) for i in range(n_b)]

    mayor_a = max(lista_a)

    if mayor_a in lista_b:
        print(f"El mayor de A ({mayor_a}) se encuentra en B.")
    else:
        print(f"El mayor de A ({mayor_a}) no se encuentra en B.")


if __name__ == "__main__":
    mayor_de_a_en_b()
