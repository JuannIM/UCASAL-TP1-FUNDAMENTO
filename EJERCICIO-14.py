def mayor_de_lista() -> None:
    """
    Solicita N números naturales y muestra el mayor de ellos.
    """
    n = int(input("Ingrese la cantidad de números: "))
    if n <= 0:
        print("Debe ingresar al menos un número.")
        return

    numeros = []
    for i in range(n):
        num = int(input(f"Ingrese el número {i + 1}: "))
        if num < 0:
            print("Debe ser un número natural.")
            return
        numeros.append(num)

    print(f"El mayor número es: {max(numeros)}")


if __name__ == "__main__":
    mayor_de_lista()
