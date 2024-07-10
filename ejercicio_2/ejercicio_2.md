# Ejercicio 2

### Transformaciones con `map`

1. Crea una función de orden superior llamada `aplicar_transformacion` que tome una lista y una función como argumentos.
   <br>
   <br>
2. La función debe devolver una nueva lista que contenga los resultados de aplicar la función a cada elemento de la lista original.
   <br>
   <br>
3. Crea los test automaticos que consideres necesarios.
   <br>
   <br>

   ```python
    def aplicar_transformacion(lista, transformacion):
    # Implementa aquí la función de orden superior
        pass

    # Ejemplo de uso:
    palabras = ["hola", "mundo", "python", "es", "genial"]
    def a_mayusculas(palabra):
        return palabra.upper()

    resultado = aplicar_transformacion(palabras, a_mayusculas)
    print(resultado)  # Debería imprimir ['HOLA', 'MUNDO', 'PYTHON', 'ES', 'GENIAL']
   ```
