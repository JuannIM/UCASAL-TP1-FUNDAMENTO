def mostrar_potencias() -> None:
    """
    Solicita un número entero x y un número N al usuario, y muestra las N primeras potencias de x.
    """
    x = int(input("Ingrese un número entero base (x): "))
    n = int(input("Ingrese la cantidad de potencias (N): "))
    
    print(f"Las {n} primeras potencias de {x} son:")
    for i in range(1, n + 1):
        print(f"{x}^{i} = {x ** i}")


if __name__ == "__main__":
    mostrar_potencias()
