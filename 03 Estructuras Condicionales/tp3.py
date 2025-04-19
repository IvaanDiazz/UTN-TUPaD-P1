#1

edad = int(input("Ingrese su edad"))

if edad >= 18:
    print("Sos mayor de edad")
else: 
    print("Sos menor de edad")



#2
    
nota = int(input("Ingrese su nota obtenida en el cuatrimestre:"))    

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")


#3

numero = int(input("Ingrese un numero"))

if numero % 2 == 0:
    print("Ha ingresado un numero par")
else:
    print("Por favor, ingrese un numero par")    


#4

edad = int(input("Ingrese su edad para informarle a que categoria pertenece"))

if edad < 12:
    print("Usted es un/a niño/a")
elif edad >= 12 and edad < 18:
    print("Usted es un/a adolescente")
elif edad >= 18 and edad < 30:
    print("Usted es un adulto joven")  
else: 
    print("Usted es un adulto")


#5

contraseña = input("Por favor ingrese una contraseña: ")

if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor ingrese una contraseña de entre 8 y 14 caracteres")


#6

import random
from statistics import mean, median, mode

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

print("Lista de números:", numeros_aleatorios)
print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)

if media > mediana > moda:
    print("Distribucion con sesgo positivo (a la derecha)")
elif media < mediana < moda:
    print("Distribucion con sesgo negativo (a la izquierda)")
elif media == mediana == moda:
    print("Distribucion sin sesgo")
else:
    print("No se puede determinar un sesgo claro con estos valores")



#7 

texto = input("Por favor ingrese una frase o palabra: ")

if texto[-1].lower() in 'aeiou':
    texto += '!'  

print("Resultado:", texto)


#8

nombre = input("Por favor ingrese su nombre: ")

print("Cómo quiere que se muestre tu nombre?")
print("1. En mayusculas")
print("2. En minúsculas")
print("3. Con la primera letra en mayuscula")


opcion = input("Ingrese 1, 2 o 3 segun su eleccion: ")

if opcion == '1':
    print("Nombre transformado:", nombre.upper())
elif opcion == '2':
    print("Nombre transformado:", nombre.lower())
elif opcion == '3':
    print("Nombre transformado:", nombre.title())
else:
    print("Opción no válida. Por favor, ingresá 1, 2 o 3.")


#9

magnitud = float(input("Ingrese la magnitud del terremoto (escala de Richter): "))

if magnitud < 3:
    print("Clasificacion: Muy leve (imperceptible)")
elif 3 <= magnitud < 4:
    print("Clasificacion: Leve (ligeramente perceptible)")
elif 4 <= magnitud < 5:
    print("Clasificacion: Moderado (sentido por personas, pero generalmente no causa daños)")
elif 5 <= magnitud < 6:
    print("Clasificacion: Fuerte (puede causar daños en estructuras debiles)")
elif 6 <= magnitud < 7:
    print("Clasificacion: Muy Fuerte (puede causar daños significativos)")
else:
    print("Clasificacion: Extremo (puede causar graves daños a gran escala)")


#10

hemisferio = input("En que hemisferio estas? (N/S): ").strip().upper()

mes = int(input("Que mes es? (1-12): "))
dia = int(input("Que dia es? (1-31): "))

def obtener_estacion(mes, dia):
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        return "Invierno"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        return "Primavera"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        return "Verano"
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        return "Otoño"

estacion_norte = obtener_estacion(mes, dia)

if hemisferio == 'N':
    print("Estacion en el hemisferio norte:", estacion_norte)
elif hemisferio == 'S':
    estaciones_opuestas = {
        "Invierno": "Verano",
        "Primavera": "Otoño",
        "Verano": "Invierno",
        "Otoño": "Primavera"
    }
    print("Estacion en el hemisferio sur:", estaciones_opuestas[estacion_norte])
else:
    print("Hemisferio no valido. Ingrese 'N' o 'S'.")