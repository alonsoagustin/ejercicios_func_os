# Ejercicio 3

### Reducción con `reduce`

1. Crea una función de orden superior llamada `aplicar_reduccion` que tome una lista y una función como argumentos.
   <br>
   <br>
2. La función debe devolver un único valor que sea el resultado de aplicar la función de reducción a todos los elementos de la lista.
   <br>
   <br>
3. Crea los test automaticos que consideres necesarios.
   <br>
   <br>

   ```python
   from functools import reduce

   def aplicar_reduccion(lista, reduccion):
       # Implementa aquí la función de orden superior
       pass

   # Ejemplo de uso:
   numeros = [1, 2, 3, 4, 5]
   def sumar(x, y):
       return x + y

   resultado = aplicar_reduccion(numeros, sumar)
   print(resultado)  # Debería imprimir 15 (1 + 2 + 3 + 4 + 5)
   ```
