def multiplos_no_divisores() -> None:
    """
    Dados 3 números naturales A, B y C, muestra los múltiplos de A menores que B
    que no sean divisores de C.
    """
    a = int(input("Ingrese el número A: "))
    b = int(input("Ingrese el número B: "))
    c = int(input("Ingrese el número C: "))

    if a <= 0 or b <= 0 or c <= 0:
        print("Todos deben ser naturales.")
        return

    print(f"Multiplos de {a} menores que {b} y que no son divisores de {c}:")
    for i in range(a, b, a):
        if c % i != 0:
            print(i)


if __name__ == "__main__":
    multiplos_no_divisores()
