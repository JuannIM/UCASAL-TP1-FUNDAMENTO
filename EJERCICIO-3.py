def contar_digitos() -> None:
    """
    Solicita un número natural al usuario y muestra la cantidad de dígitos que posee.
    """
    numero = int(input("Ingrese un número natural: "))
    if numero < 0:
        print("Debe ser un número natural.")
        return

    cantidad = 1 if numero == 0 else 0
    while numero > 0:
        cantidad += 1
        numero //= 10

    print(f"La cantidad de dígitos es: {cantidad}")


if __name__ == "__main__":
    contar_digitos()
