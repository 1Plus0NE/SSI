import sys

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

def viginere(mode, key, text):

    text = preproc(text)
    key = preproc(key)
    encrypted_text = ""

    key_length = len(key)
    key_index = 0

    for char in text:
        shift = letter_to_shift(key[key_index]) 
        shift = shift if mode == "enc" else -shift 

        # Aplica o deslocamento de uma dada letra de uma chave
        new_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        encrypted_text += new_char

        # Passar para a próxima letra da chave
        key_index = (key_index + 1) % key_length

    return encrypted_text

# Inputs
mode = sys.argv[1].lower()  # "enc" ou "dec"
key = sys.argv[2]  # Chave, desta vez como uma string
text = sys.argv[3]  # Texto a ser cifrado/decifrado

# Print viginere
result = viginere(mode, key, text)
print(result)