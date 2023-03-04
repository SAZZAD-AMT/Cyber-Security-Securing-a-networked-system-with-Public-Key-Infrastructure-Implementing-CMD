import pyperclip

def main():
    msg = 'Transposition Cipher'
    key = 10
    ciphertext = encryptMessage(key, msg)

    print("Cipher Text is: ", ciphertext, '|', pyperclip.copy(ciphertext))

def encryptMessage(key, message):
    ciphertext = [''] * key

    for col in range(key):
        position = col
        while position < len(message):
            ciphertext[col] += message[position]
            position += key
    return ''.join(ciphertext)

if __name__ == '__main__':
    main()
