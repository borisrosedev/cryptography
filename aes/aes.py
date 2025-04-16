from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def get_aes_key():
    key = get_random_bytes(32)
    return key


