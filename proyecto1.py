"""

Creacion de Proyecto: Piedra-Papel-Tijeras para utilizar todo lo aprendido sobre 
tipos de datos, operadores y condicionales en Python

Elaborado por: Angel Patino
Fecha: 11/11/2022

"""

# Task 1: Creacion del Menu de juego

print("\n****** Piedra-Papel-Tijeras ******\n")

game = True

# Task 2: Creacion del ciclo base del juego

while game == True:

    # Task 2: Creacion de variables para el juego

    player1_victories = 0
    player2_victories = 0
    played_rounds = 1

    rounds = int(input("Ingrese la cantidad de rondas a jugar: "))
    print("\nIngrese el modo de juego: \n")
    print("\t1 = Jugador vs. Computadora")
    print("\t2 = Jugador vs. Jugador\n")

    operacion = int(input("Modo de Juego: "))

    if operacion == 1:

        # Task 4: Modo de Juego PvE

        print("\n***** Jugador vs. Computadora *****\n")

    elif operacion == 2:

        # Task 4: Modo de Juego PvP

        print("\n***** Jugador vs. Jugador *****\n")

        while (player1_victories < rounds - 1) and (player2_victories < rounds - 1):
            player1 = 0
            player2 = 0
            print(f"Ronda {played_rounds}!\n")
            player1 = int(input("Jugador 1: Piedra (1), Papel (2) o Tijeras (3)?\n"))
            if player1 < 1 or player1 > 3:
                print("Error: Numero ingresado es invalido, se reinicia la ronda!")
                continue
            else:
                player2 = int(input("Jugador 2: Piedra (1), Papel (2) o Tijeras (3)?\n"))
                if player2 < 1 or player2 > 3:
                    print("\nError: Numero ingresado es invalido, se reinicia la ronda!\n")
                    continue
                else:
                    if player1 == player2:
                        print("\nEmpate! Se repetira la ronda...\n")
                        continue
                    elif player1 == 1 and player2 == 3:
                        print("\nJugador 1: Piedra\nJugador 2: Tijeras")
                        print("\nPunto para Jugador 1!\n")
                        player1_victories += 1
                    elif player1 == 2 and player2 == 1:
                        print("\nJugador 1: Papel\nJugador 2: Piedra")
                        print("\nPunto para Jugador 1!\n")
                        player1_victories += 1
                    elif player1 == 3 and player2 == 2:
                        print("\nJugador 1: Tijeras\nJugador 2: Papel")
                        print("\nPunto para Jugador 1!\n")
                        player1_victories += 1
                    elif player2 == 1 and player1 == 3:
                        print("\nJugador 1: Tijeras\nJugador 2: Piedra")
                        print("\nPunto para Jugador 2!\n")
                        player2_victories += 1
                    elif player2 == 2 and player1 == 1:
                        print("\nJugador 1: Piedra\nJugador 2: Papel")
                        print("\nPunto para Jugador 2!\n")
                        player2_victories += 1
                    elif player2 == 3 and player1 == 2:
                        print("\nJugador 1: Papel\nJugador 2: Tijeras")
                        print("\nPunto para Jugador 2!\n")
                        player2_victories += 1

            played_rounds += 1       
                  
    else:
        print("\nError: Numero ingresado no corresponde a operacion asignada! Saliendo del juego\n")

    # Task 7: Comparaciones para determinar el ganador del juego

    if player1_victories > player2_victories:
        print("\nEl Jugador 1 es el ganador!\n")
    else:
        print("\nEl Jugador 2 es el ganador!\n")

    operacion = int(input("\nDesea jugar denuevo? 1 = Si, 2 = No... "))
    if operacion == 1:
        continue
    elif operacion == 2:
        print("\nSaliendo del juego...\n")
        game = False
    else:
        print("\nError: numero ingresado no corresponde a accion alguna... Saliendo del juego\n")
        game = False