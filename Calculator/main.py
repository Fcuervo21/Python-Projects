from art import logo
#Operations
def add(n1, n2):
  return n1 + n2

def substract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

#Operations dictionary
operations={
  "+": add,
  "-": substract,
  "*": multiply,
  "/": divide
}


def calculator():
  print(logo)
  num1=float(input("Ingresa el primer numero: "))
  print("Que operacion quieres hacer?: ")
  #Imprimir simbolos
  for symbol in operations:
    print(symbol)
  should_continue=True

  while should_continue:
    operation_symbol=input("\nSelecciona simbolo: ")
    num2= float(input("Ingresa el segundo numero: "))

    calculation= operations[operation_symbol]
    answer1=calculation(num1, num2)

    print(f'{num1} {operation_symbol} {num2} = {answer1}')
    if input(f"Escribe 'y' para continuar operaciones con {answer1} o escribe 'n' para iniciar una nueva operacion: ") == "y":
      num1=answer1
    else:
      should_continue=False
      calculator() #Recursividad para empezar nueva operacion

calculator()