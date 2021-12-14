letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 'z']

option = input("Type 'encode' to encrypt and 'decode' to decrypt: \n")
message = input("Type your message: \n").lower()
shift = int(input("Enter the shift number yo want: \n"))

#function for encrypt
def encrypt(enc_message, enc_shift):
    encrypt_message = ""
    for char in enc_message:
        posi = letter.index(char)
        new_posi = posi + enc_shift
        x = letter[new_posi]
        encrypt_message += x
    print(f"The encoded message is {encrypt_message} ")

#function for decrypt
def decrypt(dec_message, dec_shift):
    decrypt_message = ""
    for char in dec_message:
        pos = letter.index(char)
        new_pos = pos - dec_shift
        y = letter[new_pos]
        decrypt_message += y
    print(f"The decoded message is {decrypt_message} ")

# Choose weather youo want to encode or decode
if option == 'encode':
    encrypt(enc_message = message, enc_shift= shift)
elif option == 'decode':
    decrypt(dec_message= message, dec_shift = shift)
