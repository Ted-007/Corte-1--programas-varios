def es_palindromo(palabra):
    """
    Verifica si la palabra o frase ingresada es un palíndromo.

    Args:
        palabra (str): La palabra o frase a evaluar.

    Returns:
        bool: True si la palabra es un palíndromo, False en caso contrario.
    """
    # Convertimos la palabra a minúsculas y eliminamos espacios y caracteres no alfabéticos
    palabra_limpia = ''.join(c for c in palabra.lower() if c.isalnum())

    # Comparamos la palabra con su versión invertida
    return palabra_limpia == palabra_limpia[::-1]


# Solicitar la palabra al usuario
palabra_usuario = input("Ingrese una palabra o frase: ")

# Determinar si es un palíndromo
if es_palindromo(palabra_usuario):
    print(f"'{palabra_usuario}' es un palíndromo.")
else:
    print(f"'{palabra_usuario}' no es un palíndromo.")
