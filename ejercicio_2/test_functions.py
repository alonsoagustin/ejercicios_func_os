from ejercicio_2.functions import aplicar_transformacion

def test_aplicar_transformacion_con_cadenas():
    palabras = ["hola", "mundo", "python", "es", "genial"]

    def a_mayusculas(cadena:str) -> str:
        return cadena.upper()

    def duplicar(cadena:str) -> str:
        return cadena * 2

    resultado = aplicar_transformacion(palabras,a_mayusculas)
    assert resultado == ['HOLA', 'MUNDO', 'PYTHON', 'ES', 'GENIAL']

    resultado = aplicar_transformacion(palabras,duplicar)
    assert resultado == ["holahola", "mundomundo", "pythonpython", "eses", "genialgenial"]

def test_aplicar_transformacion_con_numeros():
    numeros = [1, 2, 3, 4, 5]

    def al_cuadrado(numero:int) -> int:
        return numero * numero
    
    def es_par(n: int) -> bool:
        return n % 2 == 0

    resultado = aplicar_transformacion(numeros,al_cuadrado)
    assert resultado == [1, 4, 9, 16, 25]

    resultado = aplicar_transformacion(numeros, es_par)
    assert resultado == [False, True, False, True, False]