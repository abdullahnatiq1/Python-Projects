import random   
import string

chars = " " + string.digits + string.punctuation + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

print(f"chars: {chars}")
print(f"key: {key}")

# Encryption function
plain_text = input("Enter the text to encrypt: ")
cipher_text = ""

for letter in plain_text:
        index = chars.index(letter)
        cipher_text += key[index]

print(f"Original text: {plain_text}")
print(f"Encrypted text: {cipher_text}")


# Decryption function
cipher_text = input("Enter the text to encrypt: ")
plain_text = ""

for letter in cipher_text: 
        index = key.index(letter)
        plain_text += chars[index]

print(f"Encrypted text: {cipher_text}")
print(f"Original text: {plain_text}")

