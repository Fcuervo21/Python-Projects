#Generador de contrasenas en Python
import random
from alfanumerico import letras
from alfanumerico import numeros
from alfanumerico import simbolos
from alfanumerico import passArt

opcion="Y"
print(passArt)
print("Welcome to the Password Generator")

while opcion == "Y":
    nr_letters= int(input("How many letters would you like in your password?: \n")) 
    nr_symbols = int(input(f"How many symbols would you like?: \n"))
    nr_numbers = int(input(f"How many numbers would you like?: \n"))



    password=""
    #Letras
    letrasf=random.sample(letras, nr_letters)
    print("Letras: ", letrasf)
    #Simbolos
    simbolosf= random.sample(simbolos, nr_symbols)
    print("Simbolos: ", simbolosf)
    #Numeros
    numerosf= random.sample(numeros, nr_numbers)
    print("Numeros: ", numerosf)
    #Final
    p= letrasf + numerosf + simbolosf
    random.shuffle(p)
    print(f"Nueva Password: {password.join(p)}")
    
    opcion=input("Quieres otra contrasena? Y / N: \n\n")
