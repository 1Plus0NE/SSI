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

def caesar_cipher(mode, key_letter, text):
    # Calcula o deslocamento baseado na chave recebida
    base_shift = letter_to_shift(key_letter) 
    # Se for 'enc' então deslocamos a chave X letras para a frente, se não, a chave X letras para trás
    shift = base_shift if mode == "enc" else -base_shift 
    
    text = preproc(text) 
    encrypted_text = ""

    for char in text:
        # Texto cifrado/decifrado
        new_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        encrypted_text += new_char

    return encrypted_text

# Input error handling
if len(sys.argv) != 4:
    print("Erro: faltam argumentos.\nExemplo de utilização: python3 cesar.py enc R teste")
    sys.exit(1)

# Inputs
mode = sys.argv[1].lower()  # "enc" ou "dec"
key_letter = sys.argv[2]  # Chave
text = sys.argv[3]  # Texto a ser cifrado/decifrado

# Input validation
if mode not in ["enc", "dec"]:
    print("Erro: o primeiro argumento tem que ser 'enc' ou 'dec'.")
    sys.exit(1)

if len(key_letter) != 1 or not key_letter.isalpha():
    print("Erro: o segundo argumento tem que ser uma chave, por exemplo, 'G'.")
    sys.exit(1)

# Print ceaser's cipher
result = caesar_cipher(mode, key_letter, text)
print(result)