from collections import defaultdict


def encontrar_anagramas(lista_palabras):
    """
    Encuentra y agrupa los anagramas presentes en una lista de palabras.

    Args:
        lista_palabras (list): Lista de palabras a analizar.

    Returns:
        list: Lista de listas, donde cada sublista contiene palabras que son anagramas entre sí.
    """
    # Diccionario para agrupar las palabras por sus letras ordenadas
    anagramas = defaultdict(list)

    for palabra in lista_palabras:
        # Convertimos la palabra a minúsculas, ordenamos sus letras y la usamos como clave
        clave = ''.join(sorted(palabra.lower()))
        # Añadimos la palabra original al grupo correspondiente
        anagramas[clave].append(palabra)

    # Devolvemos solo los grupos que tengan más de un anagrama
    return [grupo for grupo in anagramas.values() if len(grupo) > 1]


# Ejemplo de uso
lista_palabras = ["roma", "mora", "amor", "omar", "maro", "casa", "saca", "rata", "tarta", "taco", "cota"]
anagramas_encontrados = encontrar_anagramas(lista_palabras)

# Imprimir los anagramas encontrados
for grupo in anagramas_encontrados:
    print("Anagramas:", grupo)
