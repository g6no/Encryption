from RailFence import *
from EncryptDecrypt import *

if __name__ == '__main__':
    message = "CRYPT0GR4PHY IS FUN"
    key = "SecretKey"
    ascii_key = [ord(char) for char in key]
    seed = ascii_key[0]*ascii_key[1]
    print('Key:', seed)
    print('ASCII[2]:', ascii_key[2])

    encrypted_message = encrypt(message, key, seed)
    print("Encrypted:", encrypted_message)


    encrypted_transposed = encryptRailFence(encrypted_message, ascii_key[2])
    print("Encrypted Transposed:", encrypted_transposed)

    encrypted_detransposed = decryptRailFence(encrypted_transposed, ascii_key[2])
    print("Encrypted Detransposed:", encrypted_detransposed)

    decrypted_message = decrypt(encrypted_detransposed, key, seed)
    print("Decrypted:", decrypted_message)
