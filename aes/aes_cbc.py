from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
import typing



def cypher_message(cipher: str, message: str):
    # cypher message in binary
    plaintext = message.encode()
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    return ciphertext

def decypher_message(cipher, key, ciphertext,):
    decipher = AES.new(key, AES.MODE_CBC, cipher.iv)
    decrypted = unpad(decipher.decrypt(ciphertext), AES.block_size)
    return decrypted