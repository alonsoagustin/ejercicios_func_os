from functools import reduce

def aplicar_reduccion(lista,reduccion,inicial = 0):
    """
    Aplica una función de reducción a los elementos de la lista para reducirlos a un único valor.

    Args:
        lista: Lista de elementos a reducir.
        reduccion: Función de reducción que toma un acumulador y un elemento y devuelve el nuevo acumulador.
        inicial: Valor inicial para la reducción.

    Returns:
        Resultado de la reducción de todos los elementos de la lista.
    """
    return reduce(reduccion, lista, inicial)