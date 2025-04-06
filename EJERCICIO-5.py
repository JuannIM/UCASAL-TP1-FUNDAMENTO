def sumar_digitos() -> None:
    """
    Solicita un número natural al usuario y muestra la suma de todos sus dígitos.
    """
    numero = int(input("Ingrese un número natural: "))
    if numero < 0:
        print("Debe ser un número natural.")
        return

    suma = 0
    while numero > 0:
        suma += numero % 10
        numero //= 10

    print(f"La suma de los dígitos es: {suma}")


if __name__ == "__main__":
    sumar_digitos()
