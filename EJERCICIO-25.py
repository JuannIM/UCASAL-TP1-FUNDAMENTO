def factorial() -> None:
    """
    Dado un número natural, calcula su factorial.
    """
    x = int(input("Ingrese un número natural: "))
    if x < 0:
        print("Debe ser un número natural.")
        return

    resultado = 1
    for i in range(2, x + 1):
        resultado *= i

    print(f"El factorial de {x} es: {resultado}")


if __name__ == "__main__":
    factorial()
