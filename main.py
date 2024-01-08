
# Importa el módulo Logos
from Logos import *

# Importa el módulo game_data
from game_data import *

# Importa el módulo random
import random

# Importa el módulo os
import os

# Selecciona un elemento aleatorio de la lista data y lo asigna a element_A
element_A=random.choice(data)

# Selecciona otro elemento aleatorio de la lista data y lo asigna a element_B
element_B=random.choice(data)

# Define la función compare que compara dos elementos
def compare(element_A, element_B):

    # Obtiene las posiciones de los elementos en la lista data
    position_element_A=data.index(element_A, 0, 49)
    position_element_B=data.index(element_B, 0, 49)

    # Accede al número de seguidores de los elementos
    follower_count_A=data[position_element_A]["follower_count"]
    follower_count_B=data[position_element_B]["follower_count"]

    if element_A==element_B:
        element_B=random.choice(data)
        
    # Compara los números de seguidores de los dos elementos
    elif follower_count_B>follower_count_A:
        
        return "B"
    else:
        
        return "A"

# Define la función game que ejecuta el juego
def game(element_A, element_B): 

    # Imprime el logo
    print(logo)
    game=True
    score=0
    while game==True:

        # Imprime los elementos A y B
        print(f" The element A is {element_A}")
        print(f" The element B is {element_B}")
        print()

        # Obtiene las posiciones de los elementos en la lista data
        position_element_A=data.index(element_A, 0, 49)
        position_element_B=data.index(element_B, 0, 49)        

        # Accede al número de seguidores de los elementos
        follower_count_A=data[position_element_A]["follower_count"]
        follower_count_B=data[position_element_B]["follower_count"]

        # Imprime la información de los elementos A y B
        print(f"Compare A: {data[position_element_A]['name']}, {data[position_element_A]['description']} from {data[position_element_A]['country']}")
        print(vs)
        print(f"Compare B: {data[position_element_B]['name']}, {data[position_element_B]['description']} from {data[position_element_B]['country']}")
        print()

        # Solicita al usuario que adivine quién tiene más seguidores
        user_answer = input("Who has more followers? Type 'A' or 'B': ").upper()

        # Compara la respuesta del usuario con la respuesta correcta
        if user_answer == compare(element_A, element_B):    
            os.system('cls')
            print(logo)

            # Si la respuesta es correcta, incrementa el puntaje
            score+=1
            print(f"Correct, {data[position_element_A]['name']} has {follower_count_A} and {data[position_element_B]['name']} has {follower_count_B}. your score is {score}")
            print()

            # El elemento B se convierte en el nuevo elemento A
            element_A=element_B
            
            element_B=random.choice(data)
            
            if element_A==element_B:
                element_B=random.choice(data)

        else:
            # Si la respuesta es incorrecta, termina el juego
            print(f"Sorry, numbs of followers {follower_count_A} and {follower_count_B} respectively. your final score is  {score}")
            game=False

# Ejecuta el juego
game(element_A, element_B)
