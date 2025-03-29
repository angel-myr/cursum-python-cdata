###
###         Básico - Nivel Chilindrina Huachana
###

# Ejercicio 1
palabra = 'dejé colgado en tu cielo, en una nube tu nombre...'
palabra_may = palabra.upper()
print(palabra_may)
# Ejercicio 2
string1 = "aprender"
string2 = "python"
resultado = string1.capitalize() + ' ' + string2.capitalize()
print(resultado)
# Ejercicio 3
frase = "Python es divertido"
frase_modificada = frase.replace('divertido', 'genial')
print(frase_modificada)
# Ejercicio 4
palabra = "computadora"
print(palabra[4])
# Ejercicio 5
palabra = "computadora"
print(palabra[5:9])
# Ejercicio 6
palabra = "aventura"
print(palabra[1:6:2].upper())
# Ejercicio 7
palabra = "y a pesar de todo sigue cobrando mucho mejor, no tiene talento pero es buena moza"
letra = "e"
print(palabra.count(letra))
# Ejerccio 8
frase = "si me ven solo y triste no me hablen, y fuiste tú mi baile inolvidable"
print(frase.count(' ') + 1)
# Ejercicio 9
frase = " como si nada, ella se preparó... ahora ella le dice lo lamento, lo siento. "
palabras_en_frase = frase.strip().count(' ') + 1
print(palabras_en_frase)
# Ejercicio 10
nombre = input('Escribe tu nombre: ')
print(nombre)
# Ejercicio 11
nacimiento = int(input("¿En qué año naciste?"))
print(nacimiento + 1)
# Ejercicio 12
km = int(input("Introduce la cantidad de Kilómetros recorridos: "))
print(km * 0.621371)
# Ejercicio 13
nombre = 'Makanaki'
edad = 19
print("Hola {}, tienes {} años".format(nombre, edad))
# Ejercicio 14
producto = 'Twitter'
cantidad = 1
precio = 191500200
print(f"Hay {cantidad} {producto} con un precio total de {precio * cantidad}")
# Ejercicio 15
nombre = "Exodia"
actividad  = "destruir"
hora_dia = "18:00 AM"
print(f"{nombre} prefiere {actividad} a las {hora_dia}.")
