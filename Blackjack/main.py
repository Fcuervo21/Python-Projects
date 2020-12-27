import random
import os
from ascii import logo

def clear_screen():
    """Funcion para limpiar pantalla de terminal"""
   # Para mac y linux(here, os.name is 'posix')
    if os.name == 'posix':
      _ = os.system('clear')
    else:
      # Windows
      _ = os.system('cls')

def repartir_cartas():
  """Funcion para repartir las cartas a los jugadores"""
  cartas = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  baraja= random.choice(cartas)
  return baraja

def calculo_puntaje(cartas):
    """Se toman las cartas del usuario y computadora para sumarse"""
    if sum(cartas)>21 and len(cartas)==2:
        return 0 #El cero se tomara como blackjack=21
    if 11 in cartas and sum(cartas)>21:
        cartas.remove(11)
        cartas.append(1)
    return sum(cartas)


def comparar_puntajes(puntaje_persona, puntaje_computadora):
    """Funcion para comparar puntajes y determinar final"""
    if puntaje_persona > 21 and puntaje_computadora>21:
        return "Arriba de 21. Has perdido"
    
    if puntaje_persona==puntaje_computadora:
        return "Empate"
    elif puntaje_persona==0:
        return "Has ganado con BLACKJACK"
    elif puntaje_computadora==0:
        return "La computadora ha ganado con BLACKJACK"
    elif puntaje_persona > 21:
        return "Te has pasado de 21. La computadora ha ganado"
    elif puntaje_computadora >21:
        return "La computadora se ha pasado de 21. Has ganado"
    elif puntaje_persona > puntaje_computadora:
        return "Has ganado"
    else:
        return "Has perdido"


def play_game():

    cartas_jugador=[]
    cartas_computadora=[]
    final= False
    print(logo)
    
    for i in range(2):
        cartas_jugador.append(repartir_cartas())
        cartas_computadora.append(repartir_cartas())
    
    while not final:
        puntaje_persona= calculo_puntaje(cartas_jugador)
        puntaje_computadora=calculo_puntaje(cartas_computadora)
        print(f"\nTus cartas son: {cartas_jugador}, tienes un puntaje de {puntaje_persona}")
        print(f"Primer carta de la computadora: {cartas_computadora[0]}")

        #Revisar blackjack o puntaje superior
        if puntaje_persona==0 or puntaje_computadora==0 or puntaje_persona>21:
            final=True
        else: #Revisar si la persona quiere seguir jugando
            nueva_carta=input("\nIngresa 'si' para tomar otra carta, 'no' para quedarte con tus cartas: ").lower()
            if nueva_carta=="si":
                cartas_jugador.append(repartir_cartas())
            else:
                final=True


    #Aumentar cartas a computadora hasta 17
    while puntaje_computadora != 0 and puntaje_computadora <17:
        cartas_computadora.append(repartir_cartas())
        puntaje_computadora=calculo_puntaje(cartas_computadora)
    
    print(f"\nTu mano final es: {cartas_jugador}, con un puntaje de: {puntaje_persona}")
    print(f"Mano final computadora: {cartas_computadora}, puntaje: {puntaje_computadora}")
    print(comparar_puntajes(puntaje_persona, puntaje_computadora))


while input("\n\nQuieres iniciar un juego de Blackjack? Ingresa 'si' o 'no' : ").lower() == "si":
    clear_screen()
    play_game()








