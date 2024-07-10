from ejercicio_3.functions import aplicar_reduccion

def test_aplicar_reduccion_con_numeros():
    numeros = [1, 2, 3, 4, 5]

    def sumar(x, y):
        return x + y

    resultado = aplicar_reduccion(numeros, sumar, 0)
    assert resultado == 15

    def multiplicar(x, y):
       return x * y

    resultado = aplicar_reduccion(numeros, multiplicar, 1)
    assert resultado == 120

def test_aplicar_reduccion_con_cadenas():
    cadenas = ["a", "b", "c"]
    
    def concatenar(a: str, b: str) -> str:
        return a + b

    resultado = aplicar_reduccion(cadenas, concatenar, "")
    assert resultado == "abc"