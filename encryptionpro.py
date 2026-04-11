import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars) 
key = chars.copy()

random.shuffle(key)

#ENCRYPT
plain = input("Enter a message to encrypt : ")
cipher = " "

for letter in plain:
    index = chars.index(letter)
    cipher += key[index]

print(f"original message : {plain}")
print(f"encrypted message: {cipher}")

#DECRYPT
cipher = input("Enter a message to encrypt : ")
plain = " "

for letter in cipher:
    index = key.index(letter)
    plain += chars[index]

print(f"encrypted message : {plain}")
print(f"original message: {cipher}")