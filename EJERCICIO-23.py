def invertir_digitos() -> None:
    """
    Dado un número natural, lo muestra con los dígitos invertidos.
    """
    x = input("Ingrese un número natural: ")
    if not x.isdigit():
        print("Debe ser un número natural.")
        return

    invertido = x[::-1]
    print(f"Número invertido: {invertido}")


if __name__ == "__main__":
    invertir_digitos()
