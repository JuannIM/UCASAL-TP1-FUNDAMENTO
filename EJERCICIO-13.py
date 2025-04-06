def maximo_comun_divisor() -> None:
    """
    Solicita dos números naturales y muestra su máximo común divisor (MCD).
    """
    a = int(input("Ingrese el número A: "))
    b = int(input("Ingrese el número B: "))

    if a <= 0 or b <= 0:
        print("Ambos deben ser números naturales.")
        return

    while b != 0:
        a, b = b, a % b

    print(f"El máximo común divisor es: {a}")


if __name__ == "__main__":
    maximo_comun_divisor()
