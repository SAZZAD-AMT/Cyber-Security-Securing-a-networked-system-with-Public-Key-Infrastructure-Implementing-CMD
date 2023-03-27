import hashlib

# Hashed password to be cracked
hashed_password = "e4760b8c578faff251538fe7be740bf801161304e5b11553d76a10e79219de6f"


# Open the dictionary file and read in the words
with open('dictionary.txt', 'r') as f:
    words = f.read().splitlines()

# Iterate over each word and hash it
for word in words:
    # Hash the word using SHA-256
    hashed_word = hashlib.sha256(word.encode()).hexdigest()
    
    # Compare the hashed word to the target password
    if hashed_word == hashed_password:
        print(f"Password found: {word}")
    else:
        print(f"Password Not FOUND: {word}")
        
        
