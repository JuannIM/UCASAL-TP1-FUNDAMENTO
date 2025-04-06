def menor_de_lista() -> None:
    """
    Solicita N números naturales y muestra el menor de ellos.
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

    print(f"El menor número es: {min(numeros)}")


if __name__ == "__main__":
    menor_de_lista()
