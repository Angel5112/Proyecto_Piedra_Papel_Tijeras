"""

Creacion de Proyecto: Piedra-Papel-Tijeras para utilizar todo lo aprendido sobre 
tipos de datos, operadores y condicionales en Python

Elaborado por: Angel Patino
Fecha: 11/11/2022

"""

# Task 1: Creacion del Menu de juego

print("\n****** Piedra-Papel-Tijeras ******\n")
print("Ingrese el modo de juego: \n")
print("\t1 = Jugador vs. Computadora")
print("\t2 = Jugador vs. Jugador\n")

operacion = int(input("Modo de Juego: "))

if (operacion == 1):
    print("\n***** Jugador vs. Computadora *****\n")
elif (operacion == 2):
    print("\n***** Jugador vs. Jugador *****\n")
else:
    print("\nError: Numero ingresado no corresponde a operacion asignada! Saliendo del juego\n")