import sys

def preproc(s):
    # Converter tudo para a upper
    l = []
    for c in s:
        if c.isalpha():
            l.append(c.upper())
    return "".join(l)

def caesar_decrypt(text, shift):
    # Função que recebe um criptograma e uma chave entre A e Z
    decrypted_text = ""
    
    for char in text: 
            new_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
            decrypted_text += new_char

    return decrypted_text

def cesar_attack(crypto, words):
    # Brute force de todas as combinações possíveis
    for key in range(26): 
        decrypted_text = caesar_decrypt(crypto, key)
        
        # Verificação se as palavras existem no criptograma
        if any(word in decrypted_text for word in words):
            return chr(ord('A') + key), decrypted_text  # Retorna a chave e o texto decriptado
    # Empty case se não der match
    return "",""

# Inputs
crypto = sys.argv[1]
words = [preproc(word) for word in sys.argv[2:]]

# Print ceaser's cipher attack
key, decrypted_text = cesar_attack(crypto, words)
if key: print(f"{key}\n{decrypted_text}") 
else: print()
