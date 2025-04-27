from utils.alphabet import ALPHABET
from caesar.caesar import caesar

def vigenere(message, key, is_cyphered = False):
  
    repeated_key = key
    difference_length = len(message) - len(key) 

    if  difference_length > 0:
        list_key = [ char for char in key]
        print("✅", list_key)

        i = 0
        while len(message) != len(repeated_key):
            if i != len(list_key):
                repeated_key += list_key[i]       
            else:
               i = 0
               repeated_key += list_key[i]
            i += 1   
        print(repeated_key)


    list_plain = [char for char in message]
    list_repeated_key = [char for char in repeated_key]
    matrix =  [list_plain, list_repeated_key] 
    cyphered = ""
    for o, element in enumerate(matrix[0], start=0):

        for i, alpha_one in enumerate(ALPHABET, start=0):

            if alpha_one == element:
         
                for y, alpha_two in enumerate(ALPHABET, start=0):
                    if alpha_two == matrix[1][o]:
                
                        if is_cyphered == False:
                            mod = (y+i)%26
                        else:
                            mod = (i-y)%26
                        cyphered += caesar("A", mod)
                        break
                break
    print("🔐(de)cyphered", cyphered)

  
  

  



vigenere("HELLO", "MA")
vigenere("TEXLA","MA", is_cyphered=True)

