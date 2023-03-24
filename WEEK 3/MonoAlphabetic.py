key_dict = {
    'a': 'm',
    'b': 'n',
    'c': 'b',
    'd': 'v',
    'e': 'c',
    'f': 'x',
    'g': 'z',
    'h': 'a',
    'i': 's',
    'j': 'd',
    'k': 'f',
    'l': 'g',
    'm': 'h',
    'n': 'j',
    'o': 'k',
    'p': 'l',
    'q': 'p',
    'r': 'o',
    's': 'i',
    't': 'u',
    'u': 'y',
    'v': 't',
    'w': 'r',
    'x': 'e',
    'y': 'w',
    'z': 'q',
    ' ': ' ',
}

def get_key(value):
    for key, val in key_dict.items():
        if (val == value):
            return key

def monoalphabetic_encrypt(word):
    c = ''
    for i in word:
        i = key_dict[i]
        c += i
    return c

def monoalphabetic_decrypt(word):
    c = ''
    for i in word:
        i = get_key(i)
        c += i
    return c

encryptText = monoalphabetic_encrypt("rock and roll")
print("Encrypt : ",encryptText)
print("DECRYPT : ",monoalphabetic_decrypt(encryptText))
