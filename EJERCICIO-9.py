def mostrar_divisores() -> None:
    """
    Solicita un número natural y muestra todos sus divisores.
    """
    x = int(input("Ingrese un número natural: "))
    if x <= 0:
        print("Debe ser un número natural (mayor a 0).")
        return

    print(f"Los divisores de {x} son:")
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)


if __name__ == "__main__":
    mostrar_divisores()
