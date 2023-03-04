def cipher_encrypt(plain_text, shift):
    encrypted = ""
    for c in plain_text:
        if c.isupper():
            c_index = ord(c) - ord('A')
            c_shifted = (c_index + shift) % 26 + ord('A')
            encrypted += chr(c_shifted)

        elif c.islower():
            c_index = ord(c) - ord('a')
            c_shifted = (c_index + shift) % 26 + ord('a')
            encrypted += chr(c_shifted)

        elif c.isdigit():
            encrypted += str((int(c) + shift) % 10)

        else:
            encrypted += c

    return encrypted

plain_text = "i love cse"
ciphertext = cipher_encrypt(plain_text, 7)
print('Plain Text : ',plain_text)
print('Cipher text : ',ciphertext)