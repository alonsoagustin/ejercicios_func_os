def aplicar_transformacion(lista, transformacion):
    """
    Aplica una transformación a cada elemento de una lista.

    Parametros: (lista, transformacion)
        lista: Lista de elementos a transformar.
        transformacion: Función que toma un elemento y devuelve el elemento transformado.

    La funcion devuelve una lista de elementos transformados.
    """

    # Implementa aquí la función de orden superior)
    return list(map(transformacion,lista))