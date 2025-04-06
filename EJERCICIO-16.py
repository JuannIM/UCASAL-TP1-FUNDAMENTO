def promedio_lista() -> None:
    """
    Solicita una lista de N números enteros y calcula su promedio.
    """
    n = int(input("Ingrese la cantidad de números: "))
    if n <= 0:
        print("Debe ingresar al menos un número.")
        return

    suma = 0
    for i in range(n):
        num = int(input(f"Ingrese el número {i + 1}: "))
        suma += num

    promedio = suma / n
    print(f"El promedio es: {promedio:.2f}")


if __name__ == "__main__":
    promedio_lista()
