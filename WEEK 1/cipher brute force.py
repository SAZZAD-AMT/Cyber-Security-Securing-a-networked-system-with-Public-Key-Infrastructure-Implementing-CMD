#Brute force to decrypt cypher text
def cipher_decrypt_lower(ciphertext, key):
    decrypted = ""
    for c in ciphertext:
        if c.islower():
            c_index = ord(c) - ord('a')
            c_og_pos = (c_index - key) % 26 + ord('a')
            c_og = chr(c_og_pos)
            decrypted += c_og
        elif c.isupper():
            c_index = ord(c) - ord('A')
            c_og_pos = (c_index - key) % 26 + ord('A')
            c_og = chr(c_og_pos)
            decrypted += c_og
        elif c.isdigit():
            decrypted += str((int(c) - key) % 10)
        else:
            decrypted += c
    return decrypted

ciphertext="p svcl jzl"
for i in range(0, 26):
    plain_text = cipher_decrypt_lower(ciphertext, i)
    print("For key {}, decrypted text: {}".format(i, plain_text))
