import sys
from itertools import product
import string

def preproc(s):
    # Converter tudo para a upper
    l = []
    for c in s:
        if c.isalpha():
            l.append(c.upper())
    return "".join(l)

def letter_to_shift(letter):
    # Converte uma letra para a sua posição alfa numérica
    return ord(letter.upper()) - ord('A')

def vigenere_decrypt(text, key):

    text = preproc(text)
    key = preproc(key)
    decrypted_text = ""

    key_length = len(key)
    key_index = 0

    for char in text:
        shift = letter_to_shift(key[key_index]) 

        # Aplica o deslocamento de uma dada letra de uma chave
        new_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
        decrypted_text += new_char

        # Passar para a próxima letra da chave
        key_index = (key_index + 1) % key_length

    return decrypted_text


def vigenere_attack(key_size, crypto, words):

    key_size = int(key_size)

    # Brute force de todas as combinações possíveis de uma chave com size X
    for key_tuple in product(string.ascii_uppercase, repeat=key_size):
        key = "".join(key_tuple)
        decrypted_text = vigenere_decrypt(crypto, key) 
        # Verificação se as palavras existem no criptograma decifrado
        if any(word in decrypted_text for word in words):
            return key, decrypted_text  # Retorna a chave e o texto decriptado    
    # No caso de não fazer match com nenhuma das palavras
    return "",""   


# Inputs
key_size = sys.argv[1]
crypto = sys.argv[2]
words = [preproc(word) for word in sys.argv[3:]]

# Print viginere attack
key, decrypted_text = vigenere_attack(key_size, crypto, words)
if key: print(f"{key}\n{decrypted_text}") 
else: print()