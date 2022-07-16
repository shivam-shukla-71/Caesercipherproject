
from pydoc import plain
from art import logo


print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

restart=True
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text,shift_amt):
    cipher=""
    for letter in text:
        if letter==" ":
            cipher+=" "
        else:
            position=alphabet.index(letter)
            if position==25:
                new_position=shift-1
            else:
                new_position=position+shift
                cipher+=alphabet[new_position]
    return cipher

def decrypt(cipher_text,shiftat):
    plain=""
    for letter in cipher_text:
        if letter==" ":
            plain+=" "
        else:
            position=alphabet.index(letter)
            if position==0:
                old_position=26-shiftat
            else:
                old_position=position-shiftat
                plain+=alphabet[old_position]
    return plain




if direction=="encode":
    print(encrypt(text,shift))
elif direction=="decode":
    print(decrypt(text,shift))
else:
    print("Please type the correct choice")





#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 