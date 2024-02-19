import random


def generate_tableau(seed):
    # Generates a shuffled Vigenère tableau based on a seed.
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    random.seed(seed)
    tableau = []
    for _ in range(len(alphabet)):
        shuffled = list(alphabet)
        random.shuffle(shuffled)
        tableau.append(''.join(shuffled))
    return tableau


def modify_key(key, length):
    # Repeats or truncates the key to match the specified length.
    return (key * (length // len(key) + 1))[:length]


def encrypt(plaintext, key, seed):
    # Encrypts plaintext using the Vigenère cipher with a shuffled tableau.
    tableau = generate_tableau(seed)
    modified_key = modify_key(key.upper(), len(plaintext))
    ciphertext = ''

    for i, char in enumerate(plaintext.upper()):
        if char.isalpha():
            row = ord(modified_key[i]) - ord('A')
            col = ord(char) - ord('A')
            ciphertext += tableau[row][col]
        else:
            ciphertext += char

    return ciphertext


def decrypt(ciphertext, key, seed):
    # Decrypts ciphertext using the Vigenère cipher with a shuffled tableau.
    tableau = generate_tableau(seed)
    modified_key = modify_key(key.upper(), len(ciphertext))
    plaintext = ''

    for i, char in enumerate(ciphertext.upper()):
        if char.isalpha():
            row = ord(modified_key[i]) - ord('A')
            col = tableau[row].index(char)
            plaintext += chr(col + ord('A'))
        else:
            plaintext += char

    return plaintext

