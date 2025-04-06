def mayor_digito() -> None:
    """
    Dado un número natural, muestra el mayor de sus dígitos.
    """
    x = input("Ingrese un número natural: ")
    if not x.isdigit():
        print("Debe ingresar un número natural.")
        return

    mayor = max(int(digito) for digito in x)
    print(f"El mayor dígito de {x} es: {mayor}")


if __name__ == "__main__":
    mayor_digito()
