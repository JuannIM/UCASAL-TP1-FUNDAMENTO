def sumar_divisores() -> None:
    """
    Solicita un número natural y suma todos sus divisores.
    """
    x = int(input("Ingrese un número natural: "))
    if x <= 0:
        print("Debe ser un número natural mayor a cero.")
        return

    suma = 0
    for i in range(1, x + 1):
        if x % i == 0:
            suma += i

    print(f"La suma de los divisores de {x} es: {suma}")


if __name__ == "__main__":
    sumar_divisores()
