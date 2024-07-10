from ejercicio_1 import aplicar_filtro

def test_aplicar_filtro_con_pares():
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    def es_par(n: int) -> bool:
        return n % 2 == 0
    
    resultado = aplicar_filtro(numeros, es_par)
    assert resultado == [2, 4, 6, 8, 10]

def test_aplicar_filtro_con_impares():
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def es_impar(n: int) -> bool:
        return n % 2 != 0
    
    resultado = aplicar_filtro(numeros, es_impar)
    assert resultado == [1, 3, 5, 7, 9]

def test_aplicar_filtro_con_positivos():
    numeros = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

    def es_positivo(n: int) -> bool:
        return n > 0
    
    resultado = aplicar_filtro(numeros, es_positivo)
    assert resultado == [1, 2, 3, 4, 5]
