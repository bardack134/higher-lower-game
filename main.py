from Logos import *

from game_data import *
import random

import os



#ESCOGER 1 ELEMENTO ALEATORIO DE LA LISTA Y COMPARARLO CON OTRO QUE TAMBIEN SERA ALEATORIO
element_A=random.choice(data)
element_B=random.choice(data)




    

def compare(element_A, element_B):
    

    #miro las posiciones de los elementos dentro de la lista de diccionarios "data", para poder acceder a los datos del elemento especifico sabiendo su pocicion
    position_element_A=data.index(element_A, 0, 49)
    position_element_B=data.index(element_B, 0, 49)
    
    
    # print()
    # print(f"the element A is inside data_list in the position {position_element_A}")
    # print(f"the element B is inside data_list in the position  {position_element_B}")
    # print()
    
    #Accedo al dato de numbers of followers de los elementos, que es el dato que me interesa        
    follower_count_A=data[position_element_A]["follower_count"]
    follower_count_B=data[position_element_B]["follower_count"]
    
    
    
    #COMPARAR LOS DOS ELEMENTOS ESCOGIDOS INCICIALMENTE ALEATORIAMENTE (ELEMENTO A Y ELEMENTO B)
    if follower_count_B>follower_count_A:
        
        #SI LA RESPUESTA ES CORRECTA ELEMENTO B SE CONVIERTE EN ELEMENTO A Y ESOCGEMOS ALEATORIAMENTE UN NUEVO ELEMENTO B
        print()
        
        element_A=element_B
        element_B=random.choice(data)
        return "B"
    
    else:
        element_A=element_A
        element_B=random.choice(data)
        return "A"
    
    
   
def game(element_A, element_B): 
    
    #Print logo
    print(logo)
    game=True
    score=0
    while game==True:
           
        
        print(f" The element A is {element_A}")
        print(f" The element B is {element_B}")
        print()
        
        #miro las posiciones de los elementos dentro de la lista de diccionarios "data", para poder acceder a los datos del elemento especifico sabiendo su pocicion
        position_element_A=data.index(element_A, 0, 49)
        position_element_B=data.index(element_B, 0, 49)        
        
        
           
      
              
        #Accedo al dato de numbers of followers de los elementos, que es el dato que me interesa        
        follower_count_A=data[position_element_A]["follower_count"]
        follower_count_B=data[position_element_B]["follower_count"]
            
        #IMPRIMIR LOGO VS - #ORACION NOMBRE - PROFESION- PAIS CARDI B, AMUSICIAN, FROM UNITED STATES
        print(f"Compare A: {data[position_element_A]['name']}, {data[position_element_A]['description']} from {data[position_element_A]['country']}")
        
        print(vs)
        
        print(f"Compare B: {data[position_element_B]['name']}, {data[position_element_B]['description']} from {data[position_element_B]['country']}")
        print()

            
        user_answer = input("Who has more followers? Type 'A' or 'B': ").upper()
        
        #COMPARAR LA RESPUESTA DEL USUARIO CON EL VALOR CORRECTO DE QUIEN ES MAYOR

        if user_answer == compare(element_A, element_B):    
            os.system('cls')
            print(logo)
            
            score+=1
            print(f"Correct, {data[position_element_A]['name']} has {follower_count_A} and {data[position_element_B]['name']} has {follower_count_B}. your score is {score}")
            print()
            
            
                
            element_A=element_B
            element_B=random.choice(data)
                
            
            
                       
            
        else:
            print(f"Sorry, numbs of followers {follower_count_A} and {follower_count_B} respectively. your final score is  {score}")
            game=False
            
        
            
game(element_A, element_B)       


#CREAR FUNCION PARA CAMBIAR VALORES SI EL USUARIO ACERTO CON LA RESPUESTA

#CREAR VARIABLE PARA ACUMULAR LOS PUNTOS DEL USUARIO POR CADA RESPUESTA CORRECTA

#EL USUARIO DEBE CONTINUAR ADIVINANDO HASTA QUE SE EQUIBOQUE POR LO TANCO USAR CICLO WHILE
