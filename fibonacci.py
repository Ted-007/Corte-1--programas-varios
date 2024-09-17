def suma_fibonacci(n):
    """
    Calcula la suma de los primeros n términos de la serie de Fibonacci.

    Args:
        n (int): El número de términos de la serie que se desean sumar.

    Returns:
        int: La suma de los primeros n términos de la serie de Fibonacci.
    """
    # Verificación básica para valores pequeños de n
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    # Inicialización de los dos primeros términos de la serie
    a, b = 1, 1
    suma = a + b

    # Calcular el resto de la serie hasta el término n
    for i in range(3, n + 1):
        siguiente = a + b
        suma += siguiente
        a, b = b, siguiente

    return suma


# Solicitar el valor de n al usuario
n = int(input("Ingrese el número de términos que desea sumar de la serie Fibonacci: "))

# Calcular la suma de los primeros n términos
resultado = suma_fibonacci(n)

# Mostrar el resultado
print(f"La suma de los primeros {n} términos de la serie Fibonacci es: {resultado}")
