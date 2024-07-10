from typing import List, Callable

def aplicar_filtro(lista: List[int], filtro: Callable[[int], bool]) -> List[int]:
    """
    Aplica un filtro a cada elemento de la lista y devuelve una nueva lista
    que contiene solo los elementos que pasan el filtro.

    Args:
        lista: Lista de elementos a filtrar.
        filtro: Función de filtro que toma un elemento y devuelve True o False.

    Returns:
        Lista de elementos que pasan el filtro.
    """
    return list(filter(filtro, lista))
