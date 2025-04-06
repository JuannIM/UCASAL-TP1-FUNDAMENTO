def contar_divisores() -> None:
    """
    Solicita un número natural y muestra la cantidad total de sus divisores.
    """
    x = int(input("Ingrese un número natural: "))
    if x <= 0:
        print("Debe ser un número natural.")
        return

    cantidad = 0
    for i in range(1, x + 1):
        if x % i == 0:
            cantidad += 1

    print(f"La cantidad de divisores de {x} es: {cantidad}")


if __name__ == "__main__":
    contar_divisores()
