from aes.aes import get_aes_key
from aes.aes_cbc import decypher_message, cypher_message
from rsa.rsa import generated_rsa_keys
#print(get_aes_key())
#print(generated_rsa_keys())
from Crypto.Cipher import AES 
aes_key = get_aes_key()
cipher = AES.new(aes_key, AES.MODE_CBC)

crypted_message = cypher_message(cipher, "les hirondelles sont bleues")
print(crypted_message)
decrypted_message = decypher_message(cipher,aes_key,crypted_message)
print(decrypted_message)