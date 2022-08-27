#Importar randint (nos permite generar numeros aleatorios) en la libreria de random.
from random import randint

#Input del nombre del jugador y breve explicación del juego.
nombre = input("Cual es tu nombre? ")
print(f"Hola {nombre}. El juego consiste en adivinar un número del 1 al 100, si lo adivinas has ganado! Solo tienes 8 intentos.")

#Booleano
mi_bool_1 = False

#Estructura del juego.
while mi_bool_1 == False:
    numero_creado = randint(1, 101)
    intentos = 0
    mi_bool_2 = False
    while intentos<8 and mi_bool_2 == False:
        numero_intro = input("Dime tu número: ")
        numero_intro = int(numero_intro)
        if numero_intro == numero_creado:
            print(f"Has ganado! Y te ha tomado {intentos +1} intentos.")
            mi_bool_2 = True
        elif numero_intro < 1:
            print("Tú numero es inferior a 1, tienes que poner un número entre le 1 - 100")
        elif numero_intro > 100:
            print("Tú numero es más grande que 100, tienes que poner un número entre le 1 - 100")
        elif numero_creado < numero_intro:
            print("Tú numero es > que el número ganador.")
        elif numero_creado > numero_intro:
            print("Tú numero es < que el número ganador.")
        intentos = intentos + 1

    #Fin del juego y pregunta al jugador si quiere volver a jugar.
    pregunta = input("Quieres seguir jugando? (No o escribe otro caracter para continuar): ")
    if pregunta == "No":
        mi_bool_1 = True








