Letters = 'abcdefghijklmnopqrstuvwxyz'
number_letters = len(Letters)

#Define function to encryption

def encrypt(plaintext, key):
    ciphertext = ''
    for letter in plaintext:
        letter = letter.lower()
        if not letter == ' ':
            index = Letters.find(letter)
            if index == -1:
                ciphertext += letter
            else: 
                new_index = index + key
                if new_index >= number_letters:
                    new_index -= number_letters 
                ciphertext += Letters[new_index]
    return ciphertext

#Define function to decrytption
def decrypt(ciphertext, key):
    plaintext = ''
    for letter in ciphertext:
        letter = letter.lower()
        if not letter == ' ':
            index = Letters.find(letter)
            if index == -1:
                plaintext += letter
            else: 
                new_index = index - key
                if new_index < 0:
                    new_index += number_letters 
                plaintext += Letters[new_index]
    return plaintext
 
 
print() #espace
print('Caesar Cipher Application')
print()

print('Encryption or Decryption ?')

user_input = input('e/d: ').lower()
print()

if user_input == 'e':
    print('Encryption Selected')
    print()
    key = int(input('enter the key (From 1 to 26): '))
    text = input('Enter text to encrypt: ')
    
    ciphertext = encrypt(text, key)
    print(f'CIPHERTEXT: {ciphertext}')


elif user_input == 'd':
    print('Decryption Selected')
    print()
    key = int(input('enter the key (From 1 to 26): '))
    text = input('Enter text to decrypt: ')
    
    plaintext = decrypt(text, key)
    print(f'PLAINTEXT: {plaintext}')

