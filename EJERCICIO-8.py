def calcular_potencia() -> None:
    """
    Solicita dos números enteros x e y, calcula x^y y muestra el resultado.
    """
    x = int(input("Ingrese la base (x): "))
    y = int(input("Ingrese el exponente (y): "))

    resultado = x ** y
    print(f"{x} elevado a la {y} es: {resultado}")


if __name__ == "__main__":
    calcular_potencia()
