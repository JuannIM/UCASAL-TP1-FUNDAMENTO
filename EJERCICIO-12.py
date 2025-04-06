def divisores_comunes() -> None:
    """
    Solicita dos números naturales y muestra sus divisores comunes.
    """
    a = int(input("Ingrese el número A: "))
    b = int(input("Ingrese el número B: "))

    if a <= 0 or b <= 0:
        print("Ambos números deben ser naturales.")
        return

    print(f"Divisores comunes entre {a} y {b}:")
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            print(i)


if __name__ == "__main__":
    divisores_comunes()
