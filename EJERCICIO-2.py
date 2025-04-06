def mostrar_digitos_invertidos() -> None:
    """
    Solicita un número natural al usuario y muestra sus dígitos del menos significativo al más significativo.
    """
    numero = int(input("Ingrese un número natural: "))
    if numero < 0:
        print("El número debe ser natural.")
        return

    if numero == 0:
        print("0")
        return

    print("Dígitos del menos al más significativo:")
    while numero > 0:
        print(numero % 10, end=" ")
        numero //= 10
    print()


if __name__ == "__main__":
    mostrar_digitos_invertidos()
