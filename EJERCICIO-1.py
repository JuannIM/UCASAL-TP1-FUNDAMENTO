def obtener_ultimo_digito() -> None:
    """
    Solicita un número natural al usuario y muestra su último dígito.
    """
    numero = int(input("Ingrese un número natural: "))
    if numero < 0:
        print("El número debe ser natural (mayor o igual a cero).")
        return

    ultimo_digito = numero % 10
    print(f"El último dígito es: {ultimo_digito}")


if __name__ == "__main__":
    obtener_ultimo_digito()
