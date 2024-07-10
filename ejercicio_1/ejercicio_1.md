# Ejercicio 1

### Filtros Personalizados con `filter`

1. Crea una función de orden superior llamada `aplicar_filtro` que tome una lista y una función como argumentos.
   <br>
   <br>
2. La función debe devolver una nueva lista que contenga solo los elementos que pasan el filtro proporcionado por la función.
   <br>
   <br>

3. Crea los test automaticos que consideres necesarios.
   <br>
   <br>

   ```python
   def aplicar_filtro(lista, filtro):
       # Implementa aquí la función de orden superior
       pass

   # Ejemplo de uso:
   numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
   def es_par(n):
       return n % 2 == 0

   resultado = aplicar_filtro(numeros, es_par)
   print(resultado)  # Debería imprimir [2, 4, 6, 8, 10]
   ```
