import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(art.cipherlogo)

cipher_text = ""
yesorno=True
def cipher(plain_text,shift_amount,direction_state):
    cipher_text = ""
    for letter in plain_text:
     position= alphabet.index(letter)
     if shift_amount>48:
      shift_amount=shift_amount%48
     if direction_state=="encode":
       new_position = position+shift_amount
       new_letter=alphabet[new_position]
       cipher_text+=new_letter
     elif direction_state=="decode":
       new_position = position-shift_amount
       new_letter=alphabet[new_position]
       cipher_text+=new_letter
    print(f"The Encrypted Text is {cipher_text}")  
    yesorno=False

while yesorno==True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))    
  cipher(plain_text=text,shift_amount=shift,direction_state=direction)
  answer=input(print("Do you wish to continue: Yes or No"))
  if answer=="yes":
      yesorno=True
      cipher(plain_text=text,shift_amount=shift,direction_state=direction)   
  else:
      yesorno=False
      print("thank you") 