def es_capicua() -> None:
    """
    Solicita un número natural al usuario y determina si es capicúa.
    """
    numero = input("Ingrese un número natural: ")
    if not numero.isdigit():
        print("Debe ingresar un número natural.")
        return

    if numero == numero[::-1]:
        print("El número es capicúa.")
    else:
        print("El número no es capicúa.")


if __name__ == "__main__":
    es_capicua()
