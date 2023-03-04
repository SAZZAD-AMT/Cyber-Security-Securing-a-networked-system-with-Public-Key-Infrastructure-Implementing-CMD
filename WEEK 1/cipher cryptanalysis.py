ciphertext="p svcl jzl"
print("Cipher Text: ", ciphertext)
stored_letters = {}

for char in ciphertext:
    if char not in stored_letters:
        stored_letters[char] = 1
    else:
        stored_letters[char] += 1

print(stored_letters)

attempt = ciphertext.replace("p", "I")
attempt = attempt.replace("j", "C")
attempt = attempt.replace("o", "H")
attempt = attempt.replace("s", "L")
attempt = attempt.replace("u", "N")
attempt = attempt.replace("z", "S")
attempt = attempt.replace("n", "G")
attempt = attempt.replace("v", "O")
attempt = attempt.replace("c", "V")
attempt = attempt.replace("l", "E")

print("Plain Text: ", attempt)
