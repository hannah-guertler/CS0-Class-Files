def shiftCypherEncrypter(plaintext):
    
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    for letter in plaintext:
        if letter in alphabet:
            cipherNumber = alphabet[letter] + 2
            cipherLetter = alphabet[cipherNumber]
            
            return letter