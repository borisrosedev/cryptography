from utils.alphabet import ALPHABET
"""
Les listes et les tuples sont 
tous deux des  en Python 
mais ils présentent des différences importantes 
en termes de mutabilité et de performance.

Les listes sont mutables, ce qui signifie qu'elles peuvent être modifiées 
après leur création (ajout, suppression, modification d'éléments).

"""

def caesar(message, shift, is_cyphered = False):
    # j'utilise une liste type de données séquentielles
    double_alphabet = ALPHABET * 2
    if not is_cyphered:
        cyphered = ""
        for character in message:
            for index, alpha in enumerate(double_alphabet, start=0):
                if character == alpha: 
                    cyphered += double_alphabet[index + shift]
                    break
        return cyphered  
    else:
        plain = ""
        for character in message:
            for index, alpha in enumerate(double_alphabet, start=25):
                if character == alpha: 
                    plain += double_alphabet[index - shift + 1]
                    break
        return plain  

        
print(caesar("KHOOR",3, True))