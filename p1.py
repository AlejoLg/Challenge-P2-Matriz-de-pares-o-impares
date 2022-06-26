


def sumar(numeros):
    suma = 0
    numeros = numeros.split (",")
    for e in numeros:
         print(e)
         suma = suma + int(e)
    return suma

respuesta = sumar("51,2,43,7,23")
print(f"La respuesta es: {respuesta}")

