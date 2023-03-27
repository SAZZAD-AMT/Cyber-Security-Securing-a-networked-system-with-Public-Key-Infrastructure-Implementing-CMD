#https://workat.tech/developer-tools/sha256-hash-generator

import hashlib

password = "sazzad"
stored_hash = "88f1821b3122366261d5778a084a366579103e32615662f76518460a0eb3e96f"

# Hash the password using SHA-256
hash_object = hashlib.sha256(password.encode())

# Convert the hash object to a hexadecimal string
hex_dig = hash_object.hexdigest()
print(hex_dig)

if hex_dig == stored_hash:
    print("Password is correct!")
else:
    print("Password is incorrect.")
