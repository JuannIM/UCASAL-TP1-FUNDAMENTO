def contar_pares_impares() -> None:
    """
    Solicita un número natural al usuario y muestra la cantidad de dígitos pares e impares.
    """
    numero = int(input("Ingrese un número natural: "))
    if numero < 0:
        print("Debe ser un número natural.")
        return

    pares = impares = 0

    if numero == 0:
        pares = 1
    else:
        while numero > 0:
            digito = numero % 10
            if digito % 2 == 0:
                pares += 1
            else:
                impares += 1
            numero //= 10

    print(f"Dígitos pares: {pares}")
    print(f"Dígitos impares: {impares}")


if __name__ == "__main__":
    contar_pares_impares()
