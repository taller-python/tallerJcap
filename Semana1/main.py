""" Prueba hola mundo Pylint """
#print("Hola Mundo"

def valida_palindromo(palabra):
    conteo = len(palabra)-1
    palabra2 = ''
    while conteo >= 0:
        palabra2 += palabra[conteo]
        conteo -= 1
    if palabra == palabra2:
        return 'TRUE' + palabra2
    elif palabra.upper() == palabra2.upper():
        return 'TRUE MAYUSCULAS ' + palabra2
    else:
        return 'FALSE'

palabra = input()
resultado = valida_palindromo(palabra)
print(resultado)
