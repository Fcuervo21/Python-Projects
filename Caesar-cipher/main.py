alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#Double list to avoid reaching the end

import art
def caesar(text, shiftCant, direction):
  word=""
  for letra in text:
    if letra in alphabet:
      posicion=alphabet.index(letra) #Avoid errors when typing numbers or spaces
      if direction=='encode':
        nuevaPosicion=posicion+shiftCant
        letraOriginal=alphabet[nuevaPosicion]
        word+=letraOriginal
      elif direction== 'decode':
        nuevaPosicion=posicion-shiftCant
        letraOriginal=alphabet[nuevaPosicion]
        word+=letraOriginal
    else:
      word+= letra
  print(f"The {direction}d text is {word}")

End= False
print(art.logo)
while not End:
  direction = input("\n\nType 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  shift=shift % 26

  caesar(text, shift, direction)

  restart=input("Type 'yes' if you want to restart. Otherwise type 'no': ").lower()
  if restart=="no":
    End=True
    print("\nThe End")